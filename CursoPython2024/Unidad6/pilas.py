


# Pilas : Son una simulacion de estructura mediante las listas
# ACCION A SIMULAR : LIFO(Last In First Out) (Ultimo en entrar es el primero en salir)

pila = [1,2,3]
pila.append(44)
pila.append(55)
pila.append(66)   # Ultimo en entrar  LI

print(f"Pila original : {pila}")
pila.pop()        # Primero en salir  FO
print(f"Pila despues de pop : {pila}")

pila.pop()        # Primero en salir  FO
pila.pop()        # Primero en salir  FO
print(f"Pila final : {pila}")

