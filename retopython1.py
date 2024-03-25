
# Estructura de control

menu = """
       ***************************************
       *  Menu principal de la aplicacion    *
       ***************************************
       
       Elija la opcion del reto que desea ejecutar
       1000: Hello World!
       1001: Suma Simple
       1002: Area Circulo
       1003: Suma 2 numeros
       1004: Producto de 2 numeros
       1005: 
       1006:
       1007:
       1008:
       1009:
       1010:
       1011:
       1012:
       1013:
       1014:
       1015:
       1016:
       1017:
       1018:
       1019:
       1020:
       1021:
       1035:
       1036:
       1037:
       1037: 
       0: Salir del programa
"""
bandera = True


while bandera:
    print(menu)
    opcion = int (input("Elija una opción: \n"))
    if opcion == 0:
        print("Hasta pronto!!")
        break
    
    elif opcion == 1000:
        #Ejercicio 1000
        print("Hello World!") 
        
    elif opcion == 1001:
        # Ejercicio 1001
        A = int(input("Ingrese #1 de la suma : \n"))
        B = int(input("Ingrese #2 de la suma : \n"))
        X = A + B
        print(f"X = {X}")
        
    elif opcion == 1002:
        # Ejercicio 1002
        pi = 3.14159
        radio = float(input("Ingrese el radio de la circunferencia: \n"))
        area = pi * radio**2
        print(f"A={area:.4f}")
        
    elif opcion == 1003:
        # Ejercicio 1003
        A = int(input())
        B = int(input())
        SOMA = A + B
        print(f"SOMA = {SOMA}") 
        
    elif opcion == 1004:
        # Reto 1004
        A = int(input())
        B = int(input())
        PROD = A * B
        print(f"PROD = {PROD}")
        
    elif opcion == 1005:
        # Reto 1005
        A = float(input())
        B = float(input())
        peso_A = 3.5
        peso_B = 7.5
        media = (peso_A * A + peso_B * B) / (3.5 + 7.5)
        print(f"MEDIA = {media:.5f}")
        
    elif opcion == 1006
        # Reto 1006
        A = float(input())
        B = float(input())
        C = float(input())
        Peso_A = 2
        Peso_B = 3
        Peso_C = 5
        MEDIA = (Peso_A*A + Peso_B*B + Peso_C*C)/(Peso_A + Peso_B + Peso_C)
    
    elif opcion == 1007
        # Reto 1007
        A = int(input())
        B = int(input())
        C = int(input())
        D = int(input())
        Resta = (A * B - C * D)
        print(f"DIFERENCA = {Resta}")
    
    elif opcion == 1008:
        # Reto 1008
        numero_empleado = int(input())
        horas_trabajadas = int(input())
        monto = float(input())
        salario = horas_trabajadas * monto
        print(f"NUMBER = {numero_empleado}")
        print(f"SALARY = U$ {salario:.2f}")
        
    elif opcion == 1009:
        # Reto 1009
        vendedor = str(input())
        salario_fijo = float(input())
        total_ventas_mes = float(input())
        porcentaje = 0.15
        salario_final = salario_fijo + total_ventas_mes * porcentaje
        print(f"TOTAL = R$ {salario_final:.2f}")
        
    elif opcion == 1010:
        # Reto 1010
        codigo_producto1, unidades_producto1, precio_producto1 = map(float, input().split())
        codigo_producto2, unidades_producto2, precio_producto2 = map(float, input().split())

        total_a_pagar = (unidades_producto1 * precio_producto1) + (unidades_producto2 * precio_producto2)

        print(f"VALOR A PAGAR: R$ {total_a_pagar:.2f}")
        
    elif opcion == 1011:
        pi = 3.14159
        R = float(input("Ingrese el radio de la esfera : \n"))
        VOLUME = (4.0 / 3) * pi * R ** 3
        print(f"VOLUME = {VOLUME:.3f}")
        
    elif opcion == 1012:
        #Reto 1012
        A, B, C = map(float, input().split())

        area_triangulo = (A * C) / 2
        area_circulo = 3.14159 * C**2
        area_trapecio = ((A + B) * C) / 2
        area_cuadrado = B**2
        area_rectangulo = A * B

        print(f"TRIANGULO: {area_triangulo:.3f}")
        print(f"CIRCULO: {area_circulo:.3f}")
        print(f"TRAPEZIO: {area_trapecio:.3f}")
        print(f"QUADRADO: {area_cuadrado:.3f}")
        print(f"RETANGULO: {area_rectangulo:.3f}")
    
    elif opcion == 1013:
        # Reto 1013
        a, b, c = map(int, input().split())

        max_value = max(a, b, c)

        print(f"{max_value} eh o maior")
        
    elif opcion == 1014:
        # Reto 1014
        X = int(input())
        Y = float(input())

        consumo_promedio = X / Y

        print(f"{consumo_promedio:.3f} km/l")
        
    elif opcion == 1015:
        # Reto 1015
        x1, y1 = map(float, input().split())
        x2, y2 = map(float, input().split())

        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
        print(f"{distancia:.4f}")
        
    elif opcion == 1016:
        # Reto 1016
        distancia_entre_ambos_autos = int(input())
        tiempo = distancia_entre_ambos_autos * 2
        print(f"{tiempo} minutos")
        
    elif opcion == 1017:
        # Reto 1017
        tiempo = int(input())
        velocidad = int(input())

        distancia_km = velocidad * tiempo

        eficiencia_combustible = 12

        consumo_combustible_litros = distancia_km / eficiencia_combustible

        print(f"{consumo_combustible_litros:.3f}")
        
    elif opcion == 1018:
        # Reto 1018
        valor = int(input())
        billetes = [100, 50, 20, 10, 5, 2, 1]
        desglose = {}
        for billete in billetes:
            desglose[billete], valor = divmod(valor, billete)
        print(f"{sum(desglose[b] * b for b in billetes)}")
        for billete, cantidad in desglose.items():
            print(f"{cantidad} nota(s) de R$ {billete},00")

    elif opcion == 1019:
        # Reto 1019
        N = int(input())

        horas = N // 3600
        minutos = (N % 3600) // 60
        segundos = N % 60

        print(f"{horas}:{minutos}:{segundos}")

    elif opcion == 1020:
        # Reto 1020
        N = int(input())

        anos = N // 365
        meses = (N % 365) // 30
        dias = (N % 365) % 30

        print(f"{anos} ano(s)")
        print(f"{meses} mes(es)")
        print(f"{dias} dia(s)")
        
    elif opcion == 1021:
        # Reto 1021
        valor = float(input())
        valores = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
        centavos = round(valor * 100)
        desglose = {}
        for valor in valores:
            valor_centavos = round(valor * 100)
            desglose[valor], centavos = divmod(centavos, valor_centavos)
        print("NOTAS:")
        for valor in valores[:6]:  
            print(f"{int(desglose[valor])} nota(s) de R$ {valor:.2f}")
        print("MOEDAS:")
        for valor in valores[6:]:  
            print(f"{int(desglose[valor])} moeda(s) de R$ {valor:.2f}")
            
    elif opcion == 1035:
        # Reto 1035
        A, B, C, D = map(int, input().split())

        if (B > C) and (D > A) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0):
            print("Valores aceitos")
        else:
            print("Valores nao aceitos")
            
    elif opcion == 1036:
        # Reto 1036
        A, B, C = map(float, input().split())

        discriminante = B**2 - 4*A*C
        if discriminante < 0 or A == 0:
            print("Impossivel calcular")
        else:
            R1 = (-B + discriminante**0.5) / (2*A)
            R2 = (-B - discriminante**0.5) / (2*A)
            print(f"R1 = {R1:.5f}")
            rint(f"R2 = {R2:.5f}") 
            
    elif opcion == 1037:
        # Reto 1037
        numero = float(input())
        if 0 <= numero <= 25:
            intervalo = "Intervalo [0,25]"
        elif 25 < numero <= 50:
            intervalo = "Intervalo (25,50]"
        elif 50 < numero <= 75:
            intervalo = "Intervalo (50,75]"
        elif 75 < numero <= 100:
            intervalo = "Intervalo (75,100]"
        else:
            intervalo = "Fora de intervalo"
        print(intervalo)
        
        
    else:
        print("La opcion seleccionado no existe!!!")