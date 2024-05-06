correo = input("Ingrese su correo: ")

## con if
print(" CON IF ")
if "@" in correo:
    print("valido")

## con for
print(" CON FOR ")
for caracter in correo: ## --> hernan@hernan.cl
    if caracter == "@":
        print("valido")
        break
        
## con while --- spoiler -->  3° unidad
contador  =0
print(" COn WHILE ")
correo.startswith("9") # comenzar con  .... 9
while contador < len(correo): # largo del caracter
    if correo[contador] == "@":
        print("valido")
        break
    contador += 1
