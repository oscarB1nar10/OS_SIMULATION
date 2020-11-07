import time
from random import choice

class datos:
    _id = int
    _nombre: str
    _peso: int

    def __init__(self, id, nombre, peso):
        self._id = id
        self._nombre=nombre
        self._peso = peso


array = []
listo = []

array += [datos(1,"uno",30)]
array += [datos(2,"dos",40)]
array += [datos(3,"tres",10)]

a=0

while ( a < len(array) ):
    print("en proceso")
    print(str(array[a]._id) + ": " + array[a]._nombre, " , ", array[a]._peso)

    #cho = choice([0,1]), cho == 1

    array[a]._peso -=10

    if  array[a]._peso==0:
        print("remove")
        listo += [array[a]]
        array.remove(array[a])
    else:
        a+=1

    print("___________________________")
    print("array")

    for i in range(len(array)):
        print(str(array[i]._id) + ": " + array[i]._nombre , " , ", array[i]._peso)

    print("___________________________")

    print("Listos")
    for i in range(len(listo)):
        print(str(listo[i]._id)  + ": " + listo[i]._nombre , " , ", listo[i]._peso)
    
    print("___________________________")

    if ( a >= len(array) and len(listo) != a ):
        a=0

    time.sleep(2)




