


# Estructura if

numero_1 = 10
numero_2 = 20

if numero_1 >= numero_2:
    print(f" El numero 1 es mayor que el 2 : {numero_1}")
    
if numero_1 > numero_2:
    print(f" El numero 1 es mayor que el 2 : {numero_1}")
    
if numero_1 != numero_2:
    print(f" El numero 1 es mayor que el 2 : {numero_1}")
    
if numero_1 == numero_2:
    print(f" El numero 1 es mayor que el 2 : {numero_1}")
    
    
# if - else

if numero_1 > 0:  #Condicion es verdadera
    print("Condicion verdadera")
else:
    print("Condicion falsa")
    
    
# if - elif - else

if numero_1 > 0: 
    print("a")
elif numero_2 > 10:
    print("b")
elif numero_2 != 10:
    print("c")
elif numero_2 > 10:
    print("b")
    if numero_2 != -2:
else:
    print("Ruta por defecto!!")