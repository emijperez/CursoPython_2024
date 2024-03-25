

# Listas

lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]

lista_1.pop()
print(lista_1)

lista_1.append(11)
print(lista_1)

lista_1.sort(reverse=True)
print(lista_1)

lista_1.remove(8)
print(lista_1)

lista_1.insert(5,100)
print(lista_1)


# Tuplas
my_tupla = (1,2,3,4,5,6,7,7,7,7,7,7,8)

my_tupla.index(8)
print(my_tupla)
my_tupla.count(7)
print(my_tupla)

print(my_tupla[5])
print(my_tupla[1:5])
print(my_tupla[:-2])

# Diccionarios
my_diccionario = {'1':1, '2':2, '3':3, '4':4}
my_diccionario.update({'1':111, '2':222, '3':333,})

dic1 = my_diccionario.copy()
print(f"Nuevo diccionario : {dic1}")
print(my_diccionario)

my_diccionario.pop('1')
my_diccionario.pop('5')
print(my_diccionario)

print(f" Llaves dic : {my_diccionario.keys()}")
print(f" Valor dic : {my_diccionario.values()}")
print(f" Items dic : {my_diccionario.itens()}")

my_diccionario.popitem()  # Borra el ultimo elemento
print(my_diccionario)

my_diccionario.popitem()  # Borra el ultimo elemento
print(my_diccionario)