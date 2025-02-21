
import socket
import socks
import concurrent.futures

PROXY_FILE = "proxycek/rawProxyList.txt"
ACTIVE_FILE = "proxycek/active.txt"
DEAD_FILE = "proxycek/dead.txt"

def get_local_ip():
    """Dapatkan IP asli tanpa bantuan website."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # OpenDNS Google
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        print(f"Gagal mendapatkan IP lokal: {e}")
        return None

def check_proxy(proxy):
    parts = proxy.strip().split(",")
    if len(parts) < 2:
        return proxy, None

    ip, port = parts[0], parts[1]

    # Validasi port
    try:
        port = int(port)
    except ValueError:
        print(f"Format salah: {proxy} (Port bukan angka)")
        return proxy, None

    s = socks.socksocket()
    s.set_proxy(socks.SOCKS5, ip, port)  # Bisa diganti SOCKS4 atau HTTP
    s.settimeout(5)  # Timeout 5 detik

    try:
        s.connect(("8.8.8.8", 80))  
        proxy_ip = s.getsockname()[0]
        s.close()
        return proxy, proxy_ip
    except Exception as e:
        print(f"Proxy gagal: {proxy} - {e}")
        return proxy, None


def main():
    """Fungsi utama pengecekan proxy."""
    original_ip = get_local_ip()
    if not original_ip:
        print("Gagal mendapatkan IP asli.")
        return

    print(f"IP asli: {original_ip}")

    with open(PROXY_FILE, "r") as f:
        proxies = f.readlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(check_proxy, proxies))

    with open(ACTIVE_FILE, "w") as active, open(DEAD_FILE, "w") as dead:
        for proxy, proxy_ip in results:
            if proxy_ip and proxy_ip != original_ip:
                active.write(f"{proxy} -> {proxy_ip}\n")
                print(f"Proxy aktif: {proxy} -> {proxy_ip}")
            else:
                dead.write(proxy + "\n")
                print(f"Proxy mati: {proxy}")

    print("Pengecekan selesai. Hasil disimpan di active.txt dan dead.txt.")

if __name__ == "__main__":
    main()

