



import json

contactos = [("Darwin", "Calle", "Profesion", "dacle1080@gmail.com"), ("Emilio", "Perez", "Docente", "emilioj_86@hotmail.com"),
             ("Darwin", "Calle", "Profesion", "dacle1080@gmail.com"), ("Emilio", "Perez", "Docente", "emilioj_86@hotmail.com"),
             ("Darwin", "Calle", "Profesion", "dacle1080@gmail.com"), ("Emilio", "Perez", "Docente", "emilioj_86@hotmail.com"),
             ("Darwin", "Calle", "Profesion", "dacle1080@gmail.com"), ("Emilio", "Perez", "Docente", "emilioj_86@hotmail.com"),
             ("Darwin", "Calle", "Profesion", "dacle1080@gmail.com"), ("Emilio", "Perez", "Docente", "emilioj_86@hotmail.com"),
             ("Darwin", "Calle", "Profesion", "dacle1080@gmail.com"), ("Emilio", "Perez", "Docente", "emilioj_86@hotmail.com"),
             ("Darwin", "Calle", "Profesion", "dacle1080@gmail.com"), ("Emilio", "Perez", "Docente", "emilioj_86@hotmail.com"),
             ("Darwin", "Calle", "Profesion", "dacle1080@gmail.com"), ("Emilio", "Perez", "Docente", "emilioj_86@hotmail.com")
             ]

datos = []

for nombre, apellido, profesion, email in contactos:
    datos.append({'nombre':nombre, 'apellido':apellido, 'profesion':profesion, 'email':email})
    
with open("archivo.json", "w") as filejson:
    json.dump(datos, filejson)
    
    
#Lectura de archivos JSON
with open("archivo.json", "w") as filejson:
    datos = json.load(filejson)
    print(f"Data: {datos}")
    print(f"TIpo: {type(datos)}")
    
    print("************************************************************************************************")
    for contacto in datos:
        print(f"{contacto['nombre']} -- {contacto['apellido']} -- {contacto['profesion']} -- {contacto['email']}")