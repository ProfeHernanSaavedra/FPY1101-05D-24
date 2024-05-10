pikachu = 4500
otaku = 5000
pulpo = 5200
Anguila = 4800

contarP = 0
contarO = 0
contarPul = 0
contarA = 0
total = 0

desc = 0

#1. Pikachu Roll $4500 2. Otaku Roll $5000 3. Pulpo Venenoso Roll $5200 4. Anguila Eléctrica Roll $4800 
resp = "si"
while resp == "si":
    contarP = 0
    contarO = 0
    contarPul = 0
    contarA = 0
    total = 0
    while True:
        try:
            print("1. Pikachu Roll $4.500")
            print("2. Otaku roll $5.000")
            print("3. Pulpo Venenoso Roll $5.200")
            print("4. Anguila Eléctrica Roll $4.800")
            print("5. Terminar Pedido")
            opcion = int(input("Ingrese su opcion: "))
            
        
            if opcion == 1:
                contarP = contarP + 1
                total = total + pikachu
            elif opcion == 2:
                contarO = contarO + 1
                total = total + otaku
            elif opcion == 3:
                contarPul = contarPul + 1
                total = total + pulpo
            elif opcion == 4:
                contarA = contarA + 1
                total = total + Anguila
            elif opcion == 5:
                break
        except ValueError:
                print("Opción no válida , debe ingrear 1 al 4")
    
    respDesc = input("Tiene codigo de descuento? : (si/no)").lower()
    if respDesc == "si":
        while True:
            codigo = input("Ingrese codigo de descuento (soyotaku)")
            if codigo == "soyotaku":
                desc = total *0.1
                break
            else:
                print("Código no válido")
                print("Desea reingresar presione 'ENTER' o salir => Presione 'X' ? ")
                respX = input().lower()
                if respX == 'x':
                    #resp = "si"
                    break

    else:
        
        desc = 0

    
    totalPagar = total - desc
    sumaCont = contarP + contarO + contarPul + contarA
    print("***************************")
    print(" TOTAL PRODUCTOS ",sumaCont)
    print("***************************")
    print("Picachu Roll : ",contarP)
    print("Otaku Roll : ",contarO)
    print("Pulpo Venenoso Roll : ",contarPul)
    print("Anguila Eléctrica Roll : ",contarA)
    print("***************************")
    print("Subtotal Por pagar : $",total)
    print("Descuento por código : $",desc)
    print("TOTAL: $",totalPagar)

    resp = input("Desea volver a comprar? si/no: ").lower()

