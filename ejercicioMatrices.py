arreglo = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

for fila in range(3):
    for columna in range(4):
        print(fila,columna)
        dato = int(input("Ingrese dato : "))
        arreglo[fila][columna] = dato

print(arreglo) # en linea

for elemento in arreglo:
    print(elemento) # en formato matriz