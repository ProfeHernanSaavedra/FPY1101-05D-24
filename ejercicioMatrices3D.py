arreglo = [
    [
        ["amarillo","rojo","verde"],
        ["naranja","verde","blanco"],
        ["rojo","blanco","amarillo"]
    ],
    [
        ["amarillo","rojo","verde"],
        ["naranja","amarillo","blanco"],
        ["rojo","blanco","amarillo"]
    ],
    [
        ["verde","rojo","verde"],
        ["naranja","verde","blanco"],
        ["rojo","amarillo","naranjo"]
    
    ]    
]
contarBlanco = 0
contarAmarillo = 0
contarRojo = 0
contarNara = 0
contarVerde = 0

for sup in arreglo: # sup es una variable cualquiera llamada superior
    for fila in sup:
        for elemento in fila:
            if elemento == "amarillo":
                contarAmarillo = contarAmarillo + 1
            else:
                if elemento == "rojo":
                    contarRojo = contarRojo + 1
                else:
                    if elemento == "naranja":
                        contarNara = contarNara + 1
                    else:
                        if elemento == "verde":
                            contarVerde = contarVerde + 1
                        else:
                            if elemento == "blanco":
                                contarBlanco = contarBlanco + 1

print("Número de elementos amarillos: ",contarAmarillo)
print("Número de elementos rojo: ",contarRojo)
print("Número de elementos naranja: ",contarNara)
print("Número de elementos verde: ",contarVerde)
print("Número de elementos blanco: ",contarBlanco)


