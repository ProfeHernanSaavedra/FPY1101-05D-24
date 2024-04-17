añoActual = int(input("Ingrese año actual: "))
añonNac = int(input("Ingrese año de nacimiento: "))

edad = añoActual - añonNac

print("Ud tiene ",edad," años de edad app")

if edad >= 18:
    print("Ud es mayor de edad")
else:
    if edad >0 and edad <= 10:
        print("Ud es un niño")
    else:
        if edad > 10 and edad <= 18:
            print("Ud es un adolescente")
        
