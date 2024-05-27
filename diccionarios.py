estudiante = {
    "nombre" :"Juan" ,
    "edad" : 21,
    "carrera": "ingenieria"

}

print(estudiante["nombre"])

estudiante["promedio"] = 3.9
print(estudiante["promedio"])

estudiante["edad"] = 22

del estudiante["carrera"]

#print(estudiante["carrera"])
estudiante["carrera"] = "Arquitectura"
print(estudiante["carrera"])

for clave,valor in estudiante.items():
    print(clave,":",valor)