import csv
import random as rd

#definir la coleccion de los cargos
CARGOS = ['ceo','desarrollador','analista de datos']

#función registrar trabajador
def registrar_trabajador(trabajadores):
    nombre = input("Ingrese el nombre y apellido del trabajador: ")
    cargo = input("Ingrese el cargo (CEO/Desarrollador/Analista de Datos): ").lower()
    while cargo not in CARGOS:
        print("Cargo no existe, vuelva a ingresar un cargo válido")
        cargo = input("Ingrese el cargo (CEO/Desarrollador/Analista de Datos): ").lower()
    #sueldoBruto = int(input("Ingrese sueldo bruto del trabajador: "))
    sueldoBruto = rd.randint(100,5000)
    #calculo de valores
    descSalud = sueldoBruto * 0.07
    descAFP = sueldoBruto * 0.12
    liquidoPagar = sueldoBruto-descSalud-descAFP

    #almacenar estos datos en diccionario
    trabajadores.append({
        'Nombre' : nombre,
        'Cargo' : cargo,
        'SueldoBruto' : sueldoBruto,
        'DescSalud' : descSalud,
        'DescAFP' : descAFP,
        'LiquidoPagar' : liquidoPagar 
    })


# función para listar todos los trabajadores.
def listar_trabajadores(trabajadores):
    print("Lista de trabajadores")
    for trabajador in trabajadores:
        print(trabajador)
        #print(trabajador['Nombre'])

def imprimir_planilla(trabajadores):
    cargoSeleccionado = input("Ingrese el cargo para imprimir la planilla( o presiona ENTER para imprimir todo): ").lower()
    if cargoSeleccionado == "":
       trabajadores_a_imprimir = trabajadores
       nombreArchivo = 'planilla_todos.txt'
    elif cargoSeleccionado in CARGOS:
        trabajadores_a_imprimir = []
        for trabajador in trabajadores:
           if trabajador['Cargo'] == cargoSeleccionado:
               trabajadores_a_imprimir.append(trabajador)
        nombreArchivo = f'planilla_{cargoSeleccionado}.txt'
    else:
        print("Cargo inválido")
        return
    
    with open(nombreArchivo,'w') as archivo:
        for trabajador in trabajadores_a_imprimir:
            archivo.write(f"Nombre y Apellido : {trabajador['Nombre']}\n")
            archivo.write(f"Cargo : {trabajador['Cargo']}\n")
            archivo.write(f"Sueldo Bruto : ${trabajador['SueldoBruto']}\n")
            archivo.write(f"Desc. Salud : ${trabajador['DescSalud']}\n")
            archivo.write(f"Desc. AFP : ${trabajador['DescAFP']}\n")
            archivo.write(f"Liquido a Pagar : ${trabajador['LiquidoPagar']}\n\n")
        
def imprimir_csv(trabajadores):
    archivoCSV = "trabajadores.csv"
    encabezado_csv = ['Nombre','Cargo','SueldoBruto','DescSalud','DescAFP','LiquidoPagar']
    with open(archivoCSV,'w') as archivo_csv:
        escritor = csv.DictWriter(archivo_csv,fieldnames=encabezado_csv)
        escritor.writeheader()

        for dato in trabajadores:
            escritor.writerow(dato)
