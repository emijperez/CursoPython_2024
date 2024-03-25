

# Variable global

valor_extra = 15

def suma(num_1, num_2):
    global valor_extra
    return num_1 + num_2 + valor_extra


# Invocaciones
Print(f"la variable global original es : {valor_extra}")
print(f"La suma  = {suma(100,300)}")
