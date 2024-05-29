datos = """
    Este curso es espectacular cuando programa
    han sido unos excelentes alumnos
    felicidades!
"""

with open('archivo.txt','w') as archivo:
    archivo.write(datos)

archivo2 = open('archivo.txt','r')
contenido = archivo2.read()
print(contenido)
archivo2.close()