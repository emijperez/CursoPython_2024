


# Colas
# Anadir elementos
# Quitar elementos
# Primero en entrar es el primero en salir (FIFO)



from collections import deque   # Importacion bajo demanda

cola = deque()  # Ya creo una cola vacia
print(f"Objeto : {cola}")
print(f" Tipo : {type(cola)}")

cola_1 = deque(['Darwin','Python','2024'])  # Ya creo una cola vacia
print(f"Objeto : {cola_1}")
print(f" Tipo : {type(cola_1)}")

# Acciones en las colas
cola.append("Loja")
cola.append("Ecuador")
cola.append("2024")

print(f"La cola tiene : {cola}")

# Simular First Out
cola.popleft()
print(f"La cola tiene : {cola}")

cola.popleft()
print(f"La cola tiene : {cola}")