import csv

# Variable global
contactos = [("Darwin", "Calle", "Profesion", "dacle1080@gmail.com"), ("Emilio", "Perez", "Docente", "emilioj_86@hotmail.com")]


with open("MyCSV.csv","w", newline="\n") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for contacto in contactos:
        writer.writerow(contacto)
        
               
def crear_archivo_csv(nombre_archivo):
    with open(nombre_archivo,"w", newline="\n") as csvfile:
        csvfile.close()
        
        
def guardar_datos_csv(nombre_archivo,datos):
    with open(nombre_archivo,"w", newline="\n") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        for dato in datos:
            writer.writerow(dato)
        

def leer_datos_csv(nombre_archivo):
    with open(nombre_archivo,"r", newline="\n") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        print(type(reader))
        for nombre, apelido, profesion, correo in reader:
            print(nombre, apelido, profesion, correo)
       
        
crear_archivo_csv("Datos.csv")
guardar_datos_csv("Datos.csv",contactos)
leer_datos_csv("Datos.csv")

