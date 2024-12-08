

## **Python Loops**

Perulangan dalam bahasa pemrograman berfungsi menyuruh komputer melakukan sesuatu secara berulang-ulang. Terdapat dua jenis perulangan dalam bahasa pemrograman python, yaitu perulangan dengan `for` dan `while`.

### Perulangan `for`
Perulangan `for` digunakan untuk mengulang suatu rangkaian (bisa berupa List, Tupel, dictio­nary, set, atau string).

####  For Loop - String


    for i in  "­Col­or":  
    	­ ­ ­ print(i) 
    
    C  
    o  
    l  
    o  
    r
    

#### For Loop - Dictionary
Perulangan key


    Car = {
		    "brand": "Ford",
    		"model": "Focus",
    		"year": 2013
    		}
    
    for i in Car:
    		print(i)
    brand
    model
    year


Perulangan value 

     Car = {
		    "brand": "Ford",
    		"model": "Focus",
    		"year": 2013
    		}
    for i in Car:
    		print(Car[i])
    Ford
    Focus
    2013

#### For Loop - Tuple

    RYB_color = ("Red","Yellow","Blue")
    for i in RYB_color:
    		print(i)
    Red
    Yellow
    Blue

#### For Loop - List

    RYB_color = ["Red","Yellow","Blue"]
    for i in RYB_color:
    		print(i)
    Red
    Yellow
    Blue

