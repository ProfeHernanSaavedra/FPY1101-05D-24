## ciclo para - for
num = 435 # esto no tiene nada que ver con el for...
print(num)
for num in range(3):
    print("El numero: ",num)
#print (num)


## ciclo mientras  - while
cont = 0
while cont < 3:
    print(cont)
    cont = cont + 1
    
##ciclo repetir

while True:
    print("   MENU    ")
    print("***********")
    print("1. Opcion 1")
    print("2. Opcion 2")
    print("3. Salir")
    resp = int(input("Ingrese opción: ?"))
    if resp == 1:
        print("haga Opcion 1 ")
    else:
        if resp == 2:
            print("haga Opcion 2 ")
        else:
            if resp == 3:
                break
    
    




