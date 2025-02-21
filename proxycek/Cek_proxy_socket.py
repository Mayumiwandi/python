import requests
import concurrent.futures
import time
import sys

PROXY_FILE = "/home/acer/mayumi/Experimen/labs-python/Proxy/rawProxyList.txt"
ACTIVE_FILE = "proxycek/active.txt"
DEAD_FILE = "proxycek/dead.txt"

def get_public_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json", timeout=5)
        return response.json().get("ip")
    except requests.RequestException:
        return None

def check_proxy(proxy):
    parts = proxy.strip().split(",")
    if len(parts) < 2:
        return proxy, False
    ip, port = parts[0], parts[1]
    proxy_url = f"{ip}:{port}"
    proxies = {"http": f"http://{proxy_url}", "https": f"https://{proxy_url}"}
    try:
        response = requests.get("https://api64.ipify.org?format=json", proxies=proxies, timeout=5)
        return proxy, response.json().get("ip")
    except requests.RequestException:
        return proxy, None

def loading_animation(duration):
    for _ in range(duration):
        for frame in "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏":
            sys.stdout.write(f"\rSedang mengecek proxy... {frame}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r\n")

def main():
    original_ip = get_public_ip()
    if not original_ip:
        print("Gagal mendapatkan IP asli.")
        return
    
    print(f"IP asli: {original_ip}")
    
    with open(PROXY_FILE, "r") as f:
        proxies = f.readlines()
    
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future = executor.submit(loading_animation, len(proxies) // 10)
        results = list(executor.map(check_proxy, proxies))
        future.cancel()
    
    with open(ACTIVE_FILE, "w") as active, open(DEAD_FILE, "w") as dead:
        for proxy, proxy_ip in results:
            if proxy_ip and proxy_ip != original_ip:
                active.write(f"{proxy} -> {proxy_ip}\n")
                print(f"Proxy aktif: {proxy} -> {proxy_ip}")
            else:
                dead.write(proxy + "\n")
                print(f"Proxy mati: {proxy}")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Pengecekan selesai dalam {elapsed_time:.2f} detik. Hasil disimpan di active.txt dan dead.txt")

if __name__ == "__main__":
    main()
