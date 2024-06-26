import pruebaFormativa3_funciones as fn

trabajadores = []

while True:
    print("Bienvenidos al sistema de sueldos")
    print("1. Registrar trabajador")
    print("2. Listar todos los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir")

    opcion = int(input("Seleccione su opción: "))

    if opcion == 1:
        fn.registrar_trabajador(trabajadores)
    elif opcion == 2:
        fn.listar_trabajadores(trabajadores)
    elif opcion == 3:
        fn.imprimir_planilla(trabajadores)
        print("Planilla generada con exito")
    elif opcion == 4:
        fn.imprimir_csv(trabajadores)
        print("Planilla generada en CSV con exito")
        break
    else:
        print("Opción no válida, seleccione nuevamente")
