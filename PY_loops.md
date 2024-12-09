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

<!-- Copyright (c) 2024 Yumi. All Rights Reserved.

This project is licensed under the MIT License.
You may obtain a copy of the License at:

    https://opensource.org/licenses/MIT
    https://github.com/Mayumiwandi -->
