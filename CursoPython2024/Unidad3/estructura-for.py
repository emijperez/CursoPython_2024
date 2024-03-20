


lista = [1,2,3,4,5,6,7,8,9]

for e in lista:
    if e == 4:
        break
    else:
        print(f"E: [{e}]")
else:
    print("Ejecucion satisfactoria!!")
    
    
# Clase enumarate()
    #    0  1  2  3  4  5  6  7  8  9   10   --->> Indices de los elementos de la lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

       #    0    1    2    3    4    5    6    7    8    9    10 --->> Indices de los elementos de la lista
tupla_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',]

for indice,valor in enumerate(lista):
    if indice % 2 == 0:
        print(f"{indice} -> {valor}")