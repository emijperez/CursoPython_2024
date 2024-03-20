

# Definicion de funcion
def multiplication(num1,num2,num3,num4):  # Parametros
    return num1*num2*num3*num4

print( f" El resultado de la multiplicacion es = {multiplication(5,3,2,3)}")  #Invocacion por posicion

print( f" El resultado de la multiplicacion es = {multiplication(num4=5,num3=3,num2=2,num1=3)}")  #Invocacion por nombre de variable
