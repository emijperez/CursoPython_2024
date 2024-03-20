
# Determinar si el numero es par o impar  --->  % modulo

numero = float(input("Ingresa el numero a determinar: par/impar \n"))

if numero > 0:
    if numero % 2 == 0:
        print(f"El numero: {numero}, es par")
    else:
        print(f"El numero: {numero}, es impar") 
else:
    print("El numero ingresa es negativo!!!")