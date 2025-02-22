import aiohttp
import asyncio
import json

KV_PAIR_PROXY_FILE = "kvProxyList.json"
RAW_PROXY_LIST_FILE = "rawProxyList.txt"
PROXY_LIST_FILE = "proxyList.txt"
IP_RESOLVER_URL = "https://myip.shylook.workers.dev"
CONCURRENCY = 99

semaphore = asyncio.Semaphore(CONCURRENCY)

async def send_request(session, url, proxy=None):
    try:
        async with semaphore:
            async with session.get(url, proxy=proxy, timeout=5) as response:
                return await response.text()
    except Exception as e:
        return None

async def check_proxy(session, proxy_address, proxy_port):
    proxy_url = f'http://{proxy_address}:{proxy_port}'
    try:
        start_time = asyncio.get_event_loop().time()
        ip_info = await send_request(session, IP_RESOLVER_URL, proxy=proxy_url)
        my_ip_info = await send_request(session, IP_RESOLVER_URL)
        end_time = asyncio.get_event_loop().time()

        if ip_info and my_ip_info:
            ip_data = json.loads(ip_info)
            my_ip_data = json.loads(my_ip_info)

            if ip_data.get("ip") and ip_data["ip"] != my_ip_data.get("ip"):
                return {
                    "error": False,
                    "result": {
                        "proxy": proxy_address,
                        "port": proxy_port,
                        "proxyip": True,
                        "delay": round((end_time - start_time) * 1000),
                        **ip_data
                    }
                }
    except Exception as e:
        return {"error": True, "message": str(e)}
    return {"error": True, "message": "Invalid proxy"}

async def read_proxy_list():
    proxies = []
    with open(RAW_PROXY_LIST_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4:
                proxies.append({"address": parts[0], "port": int(parts[1]), "country": parts[2], "org": parts[3]})
    return proxies

async def main():
    proxy_list = await read_proxy_list()
    active_proxies = []
    kv_pair = {}
    tasks = []

    async with aiohttp.ClientSession() as session:
        for proxy in proxy_list:
            tasks.append(check_proxy(session, proxy["address"], proxy["port"]))
        
        results = await asyncio.gather(*tasks)

        for result in results:
            if not result["error"]:
                data = result["result"]
                active_proxies.append(f"{data['proxy']},{data['port']},{data['country']},{data['asOrganization']}")
                if data["country"] not in kv_pair:
                    kv_pair[data["country"]] = []
                if len(kv_pair[data["country"]]) < 10:
                    kv_pair[data["country"]].append(f"{data['proxy']}:{data['port']}")
    
    with open(KV_PAIR_PROXY_FILE, "w") as f:
        json.dump(kv_pair, f, indent=2)
    with open(PROXY_LIST_FILE, "w") as f:
        f.write("\n".join(active_proxies))

    print("Proses selesai!")

if __name__ == "__main__":
    asyncio.run(main())
