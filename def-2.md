#### Fungsi Sederhana tanpa Argumen
```py
def sapa_dunia():
    print("Halo, Dunia!")

# Memanggil fungsi
sapa_dunia()  # Output: Halo, Dunia!
```
#### Fungsi dengan Satu Argumen
```py
def sapa_nama(nama):
    print(f"Halo, {nama}!")
```
#### Fungsi dengan Dua Argumen
```py
def penjumlahan(angka1, angka2): 
	hasil = angka1 + angka2 
	print(f"{angka1} + {angka2} = {hasil}") 
	
fungsi penjumlahan(5, 3)  # Output: 5 + 3 = 8 
penjumlahan(10, -2) # Output: 10 + -2 = 8

```
#### Fungsi dengan `return`
```py
def perkalian(angka1, angka2):
    hasil = angka1 * angka2
    return hasil

# Memanggil fungsi dan menyimpan hasilnya
hasil_perkalian = perkalian(4, 6)
print(f"Hasil perkalian adalah: {hasil_perkalian}") # Output: Hasil perkalian adalah: 24

# Bisa juga langsung diprint
print(perkalian(2, 7)) # Output: 14
```
#### Fungsi dengan Argumen Default
```py
def sapa(nama, pesan="Apa kabar?"):
    print(f"Halo, {nama}! {pesan}")

sapa("Andi")          # Output: Halo, Andi! Apa kabar?
sapa("Rina", "Selamat siang!") # Output: Halo, Rina! Selamat siang!
```
#### Fungsi dengan `*args` (Arbitrary Arguments)
```py
def jumlahkan_semua(*angka):
    total = 0
    for x in angka:
        total += x
    return total

print(jumlahkan_semua(1, 2, 3))         # Output: 6
print(jumlahkan_semua(1, 2, 3, 4, 5))    # Output: 15
```
#### Fungsi dengan `**kwargs` (Keyword Arguments)
```py
def tampilkan_info(**data):
    for kunci, nilai in data.items():
        print(f"{kunci}: {nilai}")

tampilkan_info(nama="Budi", umur=25, kota="Jakarta")
# Output:
# nama: Budi
# umur: 25
# kota: Jakarta
```
#### Contoh Fungsi Kompleks
```py
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)  # Rekursi

print(faktorial(5)) # Output: 120
```
#### Docstring (Dokumentasi Fungsi)
```py
def kali_dua(angka):
    """Mengalikan angka dengan dua.

    Args:
        angka: Angka yang akan dikalikan.

    Returns:
        Hasil perkalian angka dengan dua.
    """
    return angka * 2

print(kali_dua(7))  # Output: 14
print(kali_dua.__doc__) # Output: Mengalikan angka dengan dua. ...
help(kali_dua) # akan menampilkan help function termasuk docstring
```
#### Anotasi Tipe
```py
from typing import List, Tuple, Dict

def proses_data(nama: str, umur: int, nilai: float, data: List[int]) -> Tuple[str, int]:
    """Memproses data dan mengembalikan informasi."""
    total = sum(data)
    return (f"Nama: {nama}, Total Data: {total}", umur)

def buat_kamus(kunci: str, nilai: any) -> Dict[str, any]:
    """Membuat kamus."""
    return {kunci: nilai}

data = [1,2,3,4,5]

print(proses_data("Budi", 25, 8.5, data))
print(buat_kamus("nama", "andi"))
```
