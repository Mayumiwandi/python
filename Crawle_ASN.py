import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://2ip.io/analytics/asn-list/"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36"}
total_pages = 1253  # Ubah jumlah halaman yang ingin diambil

asn_data = []

# Loop untuk setiap halaman
for page in range(1, total_pages + 1):
    url = f"{base_url}?pageId={page}&orderBy=id&itemPerPage=100"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Ambil baris dari tr[2] sampai tr[101] untuk setiap halaman
    rows = soup.select("table tbody tr")[1:101]

    for row in rows:
        columns = [td.text.strip() for td in row.find_all("td")]
        asn_data.append(columns)

    print(f"✅ Halaman {page} selesai diambil!")

# Simpan hasil ke CSV
with open("asn_list_all_pages.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(asn_data)

print("🎉 Semua data berhasil disimpan ke asn_list_all_pages.csv!")
