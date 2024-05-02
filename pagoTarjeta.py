deuda = 100000
saldo = 100000

while True:
    try:
        print("             MENU            ")
        print("*****************************")
        print("1. Pago de Tarjeta de Crédito")
        print("2. Simulación de Compras")
        print("3. Salir")
        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            print("Paga")
            while True:
                try:
                    print("Su saldo es: $",saldo)
                    print("Su deuda es: $",deuda)
                    montoPago = int(input("Ingrese monto a pagar: "))
                    if montoPago < 0:
                        print("E monto debe ser mayor a cero")
                    else:
                        if montoPago > saldo:
                            print("Saldo insuficiente para pagar")
                            
                        else:
                            deuda = deuda - montoPago # deuda -= montoPago
                            print("Ud pago: $",montoPago)
                            break
                except:
                    print("Ingrese un valor válido, vuelva a intentarlo")
        else:
            if opcion == 2:
                print("Compra")
                cantidadCompra = int(input("Ingrese cantidad de compras: "))
                for i in range(cantidadCompra):
                    print("Compra ",(i+1))
                    try:
                        montoCompra = int(input("Ingrese el monto de la compra: "))
                        if montoCompra <= 0:
                            print("Deber ser mayor a cero")
                        else:
                            if saldo >= montoCompra:
                                deuda = deuda + montoCompra
                                saldo = saldo - montoCompra
                                print("Ud compro un monto de $",montoCompra)
                            else:
                                print("Saldo insuficiente")
                    except:
                        print("Ingrese un valor numerico")    
            else:
                if opcion == 3:
                    print("Saliendo....")
                    break
    except:
        print("Ingrese una opcion válida de 1 al 3")

print("Gracias Por Preferirnos, lo esperamos nuevamente!")