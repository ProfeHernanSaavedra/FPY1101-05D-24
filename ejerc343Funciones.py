'''
Objetivo del programa: Un programa funcional que, dada una lista de números 
ingresada por el usuario,identifica y muestra los números pares e impares de 
manera clara y organizada.
Reglas de negocio:
1.	Solicitar al usuario que ingrese una lista de números enteros separados por 
    espacios.
2.	Implementar una función llamada validar_lista_numeros que verifique que 
    todos los elementos ingresados sean números enteros. Si se ingresa algún
    valor no válido, solicitar nuevamente la lista.
3.	la función validar_lista_numeros debe utilizar un bucle y maneja excepciones 
    para asegurar que todos los elementos ingresados sean números enteros.
4.	Utilizar el operador de módulo % (MOD) para determinar si un número es 
    par o impar en la lista de números a ingresar.
    Considerar que un número es par cuando el mod es igual a 0, en caso contrario,
    es impar
5.	Crear dos listas separadas: una para los números pares y otra para los impares.
6.	Mostrar al usuario las listas resultantes, indicando los números pares, 
    e indicando los números impares

'''
import funciones as fn
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
            return numeros
            #print(numeros)
            #break
        
        except ValueError:
            print("Por favor ingrese numeros validos enteros")

# llamando a la funcion
lista = validar_lita_numeros()
#print(fn.validar_lita_numeros())
pares = []
impares = []

for num in lista:
    if num%2 == 0 :
        pares.append(num)
    else:
        impares.append(num)

print("Numeros pares: ", pares)
print("Numeros impares son: ", impares)


