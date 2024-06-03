import csv
import json

segmentacion_empresas = {
    "Pequeño Contribuyente" : [],
    "Mediano Contribuyente" : [],
    "Gran Contribuyente" : []

}

# leer los datos
with open("listadoRutEmpresa.csv","r") as archivo:
    escritor = csv.DictReader(archivo)
    for fila in escritor:
        ventas = int(fila["ventas"])
        clasificacion = None
        if ventas <= 100000000 :
            clasificacion = "Pequeño Contribuyente"
        elif ventas >= 100000001 and ventas <= 200000000:
            clasificacion = "Mediano Contribuyente"
        else:
            clasificacion = "Gran Contribuyente"
        
        empresa = {
            "rut"  : fila["rut"],
            "nombre" : fila["nombre"],
            "ventas" : ventas
        }

        segmentacion_empresas[clasificacion].append(empresa)

#guardar en json
with open("segmentacionEmpresa.json","w") as archivo:
    json.dump(segmentacion_empresas,archivo,indent=3)
print("Json creado.....")

