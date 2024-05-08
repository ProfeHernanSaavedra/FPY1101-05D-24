'''
Debe crear un menú de inicio de sesión, en el cual se debe mostrar los siguientes campos: 

1) iniciar sesión
2) registrar usuario
3) salir

Para lo cual usted deberá haber creado 3 variables de usuario y 3 variables de contrase-ña, ambas con valor inicial vacío, ejemplo:
•	usuario1= None 
•	usuario2=None 
•	usuario3=None
•	contrasena1= None 
•	contrasena2=None 
•	contrasena3= None

Si se selecciona la opción 1 y no existen registros de usuarios, el sistema deberá indicar que es necesario registrar un usuario antes, y volverá al menú principal, 
en el caso de que ingrese el usuario y contraseña correctamente, entonces el sistema mostrará el siguiente menú:

1) Realizar llamada
2) Enviar correo electrónico
3) Cerrar sesión


Donde la opción 1 debe solicitar un número de celular, éste deberá comenzar con 9 y su tamaño es de 9 dígitos (ejemplo: 985447561).

La opción 2, solicita un correo electrónico, el cual debe tener por lo menos un carácter de “@” (validar usando for y while) y lo 
guardará en una variable llamada “correo”.

También solicitará el mensaje a enviar y lo guardará en una variable llamada “mensaje”

Finalmente cerrar sesión, volverá al menú principal.

El sistema no acepta que se ingresen opciones distintas a 1, 2 y 3 en ambos menús, si ocu-rre esto, entonces el sistema emite un error y vuelve a solicitar la opción.

'''

usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None

while True:
    try:
        print("  MENU  ")
        print("********")
        print("1. Iniciar Sesión")
        print("2. Registrar Usuario")
        print("3. Salir")

        opcion = int(input("Seleccione  opción: "))

        if opcion  == 1:
            if usuario1 == None:
                print("No hay usuarios registrados, por favor ingrese un usuario primero")
            else:
                usuario = input("Ingrese usuario: ")
                contraseña = input("Ingrese Contraseña: ")
                if (usuario == usuario1 and contraseña == contrasena1) or (usuario == usuario2 and contraseña == contrasena2) or (usuario == usuario3 and contraseña == contrasena3):
                    print("Inicio de sesión exitoso!")
                    while True:
                        print("    SUB MENU       ")
                        print("*******************")
                        print("1. Realizar llamada")
                        print("2. Enviar correo electrónico")
                        print("3. Cerrar sesión")
                        opcionMenu2 = int(input("Seleccione Opción: "))
                        if opcionMenu2 == 1:
                            while True:
                                numero = input("Ingrese el número del celular: ")
                                if numero.startswith("9") and len(numero) == 9:
                                    print("Llamada ralizada a ",numero)
                                    break
                                else:
                                    print("Número de celular inválido, ingrese nuevamente")
                        else:
                            if opcionMenu2 == 2:
                                while True:
                                    correo = input("Ingrese el correo electrónico: ")
                                    if "@" in correo:
                                        break
                                    else:
                                        print("Correo electrónico inválido, debe tener un @")
                                mensaje = input("Ingrese el mensaje: ")
                                print("Correo electrónico enviado a ",correo," con el mensaje =>",mensaje)
                            else:
                                if opcionMenu2 == 3:
                                    print("Sesión cerrada")
                                    break
                                else:
                                    print("Opción no válida del submenú")
        else:
            if opcion == 2 :
                usuario = input("Ingrese el nuevo usuario: ")
                contraseña = input("Ingrese la nueva contraseña: ")
                if usuario1 == None:
                    usuario1 = usuario
                    contrasena1 = contraseña
                elif usuario2 == None:
                    usuario2 = usuario
                    contrasena2 = contraseña
                elif usuario3 == None:
                    usuario3 = usuario
                    contrasena3 = contraseña
                else:
                    print("Ya se han registrado los 3 usuarios como máximo")
            else:
                if opcion == 3 :
                    print("Salindo...")
                    break
                else:
                    print("Opción no válida")

    except ValueError:
        print("Ingrese una opción de menú válida!")