print("¿Cuál de los siguienes animales vive en el agua?\n")
print("\t 1.Perro")
print("\t 2.Cocodrilo")
print("\t 3.Conejo")
print("\t 4.Tiburon")
resp = int(input("Ingrese numero de respuesta: "))
puntaje = 0
if resp == 2:
    puntaje = puntaje + 0.5
else:
    if resp == 4:
        puntaje = puntaje + 1
    else:
        puntaje = 0

print("Su puntaje es :",puntaje)

