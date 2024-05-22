matriz = [
    [1,2,3],
    [4,5,6]
]

for elemento in matriz:
    print(elemento)

print()
print(matriz[1][0])

print()
for fila in range(2):
    for columna in range(3):
        print(matriz[fila][columna])

print()
for fila in matriz:
    for elemento in fila:
        print(elemento,end=' ')
print()
print(matriz)

