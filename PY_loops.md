<!-- Copyright (c) 2024 Yumi. All Rights Reserved.

This project is licensed under the MIT License.
You may obtain a copy of the License at:

    https://opensource.org/licenses/MIT
    https://github.com/Mayumiwandi -->


## **Python Loops**

Perulangan dalam bahasa pemrograman berfungsi menyuruh komputer melakukan sesuatu secara berulang-ulang. Terdapat dua jenis perulangan dalam bahasa pemrograman python, yaitu perulangan dengan `for` dan `while`.

### Perulangan `for`
Perulangan `for` digunakan untuk mengulang suatu rangkaian ***(bisa berupa List, Tupel, dictio­nary, set, atau string).***  Digunakan ketika jumlah iterasi diketahui sebelumnya. 

####  For Loop - String

```py
for i in  "­Col­or":  
	print(i) 

>>> C  
>>> o  
>>> l  
>>> o  
>>> r
```    

#### For Loop - Dictionary
##### Perulangan key
iterasi dilakukan berdasarkan ***kunci (key)*** dalam dictionary tersebut.
```py
Car = {
	"brand": "Ford",
    	"model": "Focus",
    	"year": 2013
    	}
for i in Car:
    print(i)
    
>>> brand
>>> model
>>> year
```
##### Perulangan value 
iterasi dilakukan berdasarkan ***nilai (value)*** dalam dictionary tersebut.
```py
Car = {
	"brand": "Ford",
	"model": "Focus",
	"year": 2013
	}
for i in Car:
	print(Car[i])

>>> Ford
>>> Focus
>>> 2013
```
#### For Loop - Tuple
```py
RYB_color = ("Red","Yellow","Blue")
for i in RYB_color:
	print(i)
		
>>> Red
>>> Yellow
>>> Blue
```
#### For Loop - List
```py
RYB_color = ["Red","Yellow","Blue"]
for i in RYB_color:
	print(i)
		
>>> Red
>>> Yellow
>>> Blue
```
####  The break Statement
Melalui pernyataan **break**, kita dapat menghentikan perulangan sebelum semua item selesai diolah. Pada contoh ini, perulangan berhenti saat item bernilai **'Yellow'**.
```py
RYB_color = ["Red", "Yellow", "Blue"]
for i in RYB_color:
	if(i == "Yellow"):
		break
	print(i)
	
>>> Red
```
#### The continue Statement
Dengan pernyataan **continue**, kita dapat menghentikan iterasi saat ini dan langsung melanjutkan ke iterasi berikutnya. Hal ini berguna untuk melewatkan elemen tertentu tanpa menghentikan keseluruhan perulangan.
`iterasi = perulangan`
```py
RYB_color = ["Red", "Yellow", "Blue"]
for i in RYB_color:
    if i == "Yellow":
        continue
    print(i)
    
>>>Red
>>>Blue
```

#### The range() Function
`range(n)` adalah sebuah fungsi yang mengembalikan urutan angka, dimulai dari 0 (secara default), bertambah 1 setiap kali (secara default), dan berakhir pada (n - 1).
```py
for i in range(3):
print(i)

>>> 0
>>> 1
>>> 2
```
Pada contoh ini, `range(j, n)` mengembalikan urutan angka, dimulai dari `j` dan bertambah 1 setiap kali (secara default), serta berakhir pada (n - 1).
```py
for i in range(2,5):
print(i)

>>> 2
>>> 3
>>> 4
```
Pada contoh ini, `range(j, n, k)` mengembalikan urutan angka, dimulai dari `j`, bertambah sebanyak `k` setiap kali, dan berakhir pada (n - 1).
>    **j (start)**: Angka awal dari urutan yang akan dihasilkan. Jika tidak diberikan, nilai defaultnya adalah 0.
**n (stop)**: Angka di mana urutan akan berhenti, tetapi angka ini **tidak termasuk** dalam urutan. Artinya, urutan akan berakhir pada nilai yang lebih kecil dari `n`.
**k (step)**: Jumlah kenaikan setiap angka dalam urutan. Jika tidak diberikan, nilai defaultnya adalah 1.

```py
for i in range(2,10,3):
print(i)

>>> 2
>>> 5
>>> 8
```
#### Else in For Loop
```py
for i in range(3):
    print(i)
else:
    print("finally finished!")
    
>>> 0
>>> 1
>>> 2
>>> finally finished!
```
#### Nested Loops (perulangan bersarang)
```py
list_1 = ["Data" , "Machine learning"]
list_2 = ["Scientist","Engineer"]
for i in list_1:
	for j in list_2:
		print(i,j)
		
>>> Data Scientist
>>> Data Engineer
>>> Machine Learning Scientist
>>> Machine Learning Engineer
```
#### The pass Statement
Pada Python, _**for**_ **loops** tidak boleh kosong. Artinya, setiap **`for`** loop harus memiliki setidaknya satu baris kode yang dieksekusi. Jika Anda menulis sebuah **`for`** loop yang tidak memiliki konten atau aksi di dalamnya, Python akan memberikan error karena struktur tersebut dianggap tidak lengkap.
```py
for i in RYB_color:
	pass
```
[Referensi ](https://cheatography.com/nouha-thabet/cheat-sheets/python-for-loops/pdf/?last=1576835940)

___
___
### Perulangan `while`
***While*** Loops pada Python digunakan untuk mengeksekusi blok pernyataan berulang kali hingga kondisi tertentu *terpenuhi* **(perulangan akan terus dilakukan selama kondisi terpenuhi `True`)** . Jika kondisinya menjadi `False`, baris setelah loop dalam program akan dieksekusi.
**Peringatan** 
Jika kondisi dalam **`while`** tidak pernah menjadi **`False`**, maka loop akan berjalan terus-menerus (infinite loop).

####  Example `while`
Dengan **while loop**, kita dapat mengeksekusi sekumpulan pernyataan selama kondisinya bernilai benar (**true**). Dalam contoh ini, kondisinya adalah bahwa **i** harus kurang dari 4.
```py
i = 1
while i < 4:
print(i)
	i += 1
	
>>> 1
>>> 2
```
#### The break Statement
Dengan pernyataan **break**, kita dapat menghentikan loop meskipun kondisi **while** masih bernilai benar (**true**). Dalam contoh ini, loop berhenti ketika **i** sama dengan 2.
```py
i = 1
while i < 4:
	print(i)
	if (i == 2):
		break
	i += 1
	
>>> 1
```
#### The continue Statement
Dengan pernyataan **continue**, kita dapat menghentikan iterasi saat ini dan melanjutkan ke iterasi berikutnya. Dalam contoh ini, loop melewati iterasi ketika **i** sama dengan 2 dan melanjutkan ke iterasi selanjutnya.
```py
i = 1
while i < 4:
	print(i)
	if (i == 2):
		continue
	i += 1
	
>>> 1
>>> 2
>>> 2
>>> 2
>>> 2
>>> Infinite Loop
```
```py
i = 1
while i < 4:
    print(i)
    if (i == 2):
        i += 1  # Tambahkan ini sebelum continue untuk menghindari Infinite Loop seperti di atas. 
        continue
    i += 1

>>> 1
>>> 2
>>> 3
```
#### The else Statement
Dengan pernyataan **else**, kita dapat menjalankan sebuah blok kode sekali saja ketika kondisi **while** tidak lagi bernilai benar (**True**).
```py
i = 1
while i < 4:
    print(i)
    i += 1
else:
    print("i is no longer less than 4")

>>> 1
>>> 2
>>> 3
>>> i is no longer less than 4
```
**Penjelasan**
-   Pada iterasi pertama hingga ketiga, nilai `i` adalah 1, 2, dan 3.
-   Setelah nilai `i` menjadi 4, kondisi **`i < 4`** menjadi `False`, sehingga loop berhenti dan blok **`else`** dijalankan.


#### The break
`break` akan menghentikan perulangan.

```py
index = 0
while True :
	print("Berhasil menjalankan loop")
	index += 1
	if index == 5 :
		break

>>> Berhasil menjalankan loop
>>> Berhasil menjalankan loop
>>> Berhasil menjalankan loop
>>> Berhasil menjalankan loop
>>> Berhasil menjalankan loop
```


[Referensi ](https://cheatography.com/nouha-thabet/cheat-sheets/python-while-loops/pdf/?last=1576829684)
___

### Advanced `For` Loops

```py
kata = "abcdefghij"
for item in enumerate(kata):
    print(item)

>>> (0, 'a')
>>> (1, 'b')
>>> (2, 'c')
>>> (3, 'd')
>>> (4, 'e')
>>> (5, 'f')
>>> (6, 'g')
>>> (7, 'h')
>>> (8, 'i')
>>> (9, 'j')
```
```py
kata = "abcdefghij"
for a,b in enumerate(kata):
    print(a)
    print(b)

>>> 0
>>> a
>>> 1
>>> b
>>> 2
>>> c
>>> 3
>>> d
>>> 4
>>> e
>>> 5
>>> f
>>> 6
>>> g
>>> 7
>>> h
>>> 8
>>> i
>>> 9
>>> j


```
```py

angka = [1, 2, 3, 4, 5, 6, 7]
huruf = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

for item in zip(angka, huruf):
    print(item)  # Ini sudah benar

>>> (1, 'a')
>>> (2, 'b')
>>> (3, 'c')
>>> (4, 'd')
>>> (5, 'e')
>>> (6, 'f')
>>> (7, 'g')
```
```py
yumo = 'y' in 'yumi suka python'
print(yumo)

>>> True
```
```py

kotak = {
    'a':'batu',
    'b':'kursi',
    'c':'kipas'
}
cek = 'b' in kotak
print(cek)

cek2 = 'kursi' in kotak
print(cek2)

>>> True
>>> False
```
```py
angka = list(range(1, 11))
print(angka)

>>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
```py
isi = list()
for item in range(1,11):
    isi.append(item)
    
print(isi)

>>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
```py

isi = [item for item in range(1,16)]

print(isi)

>>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
```
```py
isi = [item**2 for item in range(1,11)]

print(isi)

>>> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
```py
isi = [(item**2)/2 for item in range(1,11)]
# bisa gunakan aritmatika
print(isi)
>>> [0.5, 2.0, 4.5, 8.0, 12.5, 18.0, 24.5, 32.0, 40.5, 50.0]
```
```py
isi = [item for item in range(1,11) if item%2==0]
# menampilkan nilai genap
print(isi)
>>> [2, 4, 6, 8, 10]
```
```py
isi = [item**2 for item in range(1,41) if item%2==0]
# angka dari 1 - 40 di pangkat 2 di modulus 2 
print(isi)
>>> [4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600]
```
```py
isi = [item if item%2==0 else 'angka ini bilangan ganjil' for item in range(1,11)]
print (isi)

>>> ['angka ini bilangan ganjil', 2, 'angka ini bilangan ganjil', 4, 'angka ini bilangan ganjil', 6, 'angka ini bilangan ganjil', 8, 'angka ini bilangan ganjil', 10]
```
```py
isi = []
for item in range(1,11):
    if item%2==0 :
        isi.append(item)
    else:
        isi.append('angka ini bilangan ganjil')
for i in isi:
    print (f'\t{i}')


>>> angka ini bilangan ganjil
>>> 2
>>> angka ini bilangan ganjil
>>> 4        
>>> angka ini bilangan ganjil
>>> 6
>>> angka ini bilangan ganjil
>>> 8
>>> angka ini bilangan ganjil
>>> 10
```
[Referensi ](https://youtu.be/GSL6m4eE12I?si=LVCptEzYyNu7VGQj)
___

<!-- Copyright (c) 2024 Yumi. All Rights Reserved.

This project is licensed under the MIT License.
You may obtain a copy of the License at:

    https://opensource.org/licenses/MIT
    https://github.com/Mayumiwandi -->
