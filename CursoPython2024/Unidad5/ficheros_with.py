


# Forma moderna de gestionar ficheros
# Python manerja de forma adecuada el flujo de la informacion sobre los archivos
# With

def crear_fichero_with(nombre_fichero='Fichero_texto.txt'):
    """Crear un fichero, con la instruccion 'with', dandole la gestion y control a python

    Args:
        nombre_fichero (str, optional): _description_. Defaults to 'Fichero_texto.txt'.
    """    
    with open(nombre_fichero, 'w') as f:
        print(f"tipo dato : {type(f)}")
        print(f"Se creo con exito!!")
        
        
        

crear_fichero_with()