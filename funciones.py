# 4 tipos de funciones:

# 1. sin argumentos y sin retorno
# 2. sin argumentos y con retorno
# 3. con argumentos y si retorno
# 4. con argumentos y con retorno

# 1
def saludo():
    print("Hola")

# 2
def saludo2():
    return "hola con retorno"

# 3
def sumar(num1,num2):
    suma = num1 + num2 
    print(suma)

#4
def sumar2(num1,num2):
    suma = num1 + num2 
    return suma


def validar_lita_numeros():
    while True:
        try:
            numeros = input("Ingrese una lista de numeros enteros separados por espacios: ").split()
            # 3 4 5 
            # split --> numeros = ['3','4','5']
            for i in range(len(numeros)):
                numeros[i] = int(numeros[i])
                #numeros[0]= int(numeros[0])
                #    3     = int ('3')
            # numeros = [3,4,5]    
            #return numeros
            print(numeros)
            break
        except ValueError:
            print("Por favor ingrese numeros validos enteros")