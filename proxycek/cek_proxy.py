import os
import asyncio
import httpx
from aiofiles import open as aio_open

# File input yang berisi daftar IP dan port
file_input = "autoscan/rawProxyList.txt"
active_file = "autoscan/active.txt"
dead_file = "autoscan/dead.txt"

async def check_proxy(ip, port, country, organization):
    """Mengecek apakah proxy aktif dan menggunakan Cloudflare"""
    proxy_url = f"http://{ip}:{port}"
    result = f"{ip},{port},{country},{organization}"
    
    try:
        transport = httpx.AsyncHTTPTransport(proxy=proxy_url)
        async with httpx.AsyncClient(transport=transport, timeout=5) as client:
            response = await client.get("http://detectportal.firefox.com/success.txt")
            
            server_header = response.headers.get("server", "").lower()
            status_code = response.status_code
            
            if server_header == "cloudflare" and status_code == 400:
                print(f"[✅ AKTIF] {result}")
                return "active", result
            else:
                print(f"[❌ TIDAK AKTIF] {result}")
                return "dead", result
    
    except (httpx.RequestError, httpx.ProxyError, httpx.ConnectTimeout, httpx.ConnectError):
        print(f"[❌ GAGAL TERHUBUNG] {result}")
        return "dead", result

async def process_proxies(filename, max_workers=300):
    """Membaca file, cek semua proxy dulu, lalu tulis hasilnya sekaligus."""
    if not os.path.exists(filename):
        print(f"File '{filename}' tidak ditemukan.")
        return
    
    active_proxies = []
    dead_proxies = []
    
    tasks = []
    async with aio_open(filename, 'r') as file:
        async for line in file:
            parts = line.strip().split(',')
            if len(parts) >= 2:
                ip, port = parts[0], parts[1]
                try:
                    port = int(port)
                except ValueError:
                    print(f"[ERROR] Port tidak valid: {parts[1]}")
                    continue
                
                country = parts[2] if len(parts) > 2 else "Unknown"
                organization = parts[3] if len(parts) > 3 else "Unknown"
                
                tasks.append(check_proxy(ip, port, country, organization))
    
    sem = asyncio.Semaphore(max_workers)
    
    async def sem_task(task):
        async with sem:
            return await task
    
    results = await asyncio.gather(*(sem_task(task) for task in tasks))
    
    for status, result in results:
        if status == "active":
            active_proxies.append(result)
        else:
            dead_proxies.append(result)
    
    # Tulis hasil sekaligus setelah semua selesai
    async with aio_open(active_file, 'w') as af, aio_open(dead_file, 'w') as df:
        await af.write('\n'.join(active_proxies) + '\n')
        await df.write('\n'.join(dead_proxies) + '\n')
    
    print("✅ Proses pengecekan selesai!")

if __name__ == "__main__":
    asyncio.run(process_proxies(file_input))
