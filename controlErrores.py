
while True:
    try:
        num = int(input("Ingrese un numero: "))
        #break
    except ValueError as errorPalabra:
        print("Ingreso una palabra y es un numero")
    else:
        print("Todo bien!!")
        break
    finally:
        print("ten un lindo dia! ")

while True:
    try:
        num = int(input("Ingrese un numero: "))
        break
    except ValueError as errorPalabra:
        print("Ingreso una palabra y es un numero")
    else:
        print("Todo bien!!") 
        # como tiene un break no se ejecuta
    finally:
        print("ten un lindo dia! ")

'''
try:
    div = 10/0
except  ZeroDivisionError as dividirPorCero:
    print("Divisite por cero, no haga eso!")
'''
