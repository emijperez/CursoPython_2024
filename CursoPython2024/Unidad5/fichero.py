


# Operaciones con archivos en python

from io import open
from os import *
from paramiko import Channel, ChannelFile
from plotly import display
from trace import Trace, _Ignore
from pickle import Pickler

# Importacion de tipo alias
import os.path as darwin


# Importacion principal para trabajar con ficheros en python
from io import open
from os import path

def crear_fichero_inicial(nombre = "Inicio.txt"):
    
    """Crea un archivo vacio, de cualquier extension.
    """    
    fichero = open(nombre, "W")
    fichero.close()


def crear_fichero(nombre_fichero):
    
    cadena = "Hola mundo desde un fichero!!"
    
    fichero = open(nombre_fichero, 'W')
    fichero.write(cadena)
    fichero.close()
    
# Invocaciones a funciones
crear_fichero('saludo.txt')
crear_fichero(nombre_fichero='Darwin.txt')

crear_fichero()
crear_fichero(nombre="NombreFichero.xls")





# Crear fichero anotaciones.txt




# lectura de un fichero por metodo read


