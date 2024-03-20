


# Super fucnion, se conforma de argumentos indeterminados de tipo *args y **kwargs
# El orden sera el siguiente:
# 1.- Enviamos los datos por posicion ---> 1,2,3,4
# 2.- Enviamos los datos por nombre posterior al punto 1
def super_funcion_suma(*args, **kwargs):  # 1,2,3,4; num1=5, num2=10, num3=15
    
    """Esta super funcion suma n numeros, mediante tuplas y diccionarios"""
    suma_total = 0
    for arg in args:
        print(f"{arg}")
        suma_total += arg
    
    for k in kwargs:
        print(f"{kwargs[k]}")
        suma_total += kwargs[k]
        
    return suma_total
        
print(f"La suma total es: {super_funcion_suma(5,2,3,num1=10,num2=20,num3=30)}")

