import csv

with open('nuevo_archivo.csv','w',newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    escritor_csv.writerow(['Nombre','Edad','Comuna'])
    escritor_csv.writerows([
        ['Juan',24,'Quilpue'],
        ['Maria',10,'Valpo'],
        ['Pedro',30,'Vina'],
        ['Diego',16,'Limache'],
        ['Carlos',31,'Quintero']
    ])

##para abrir archivo
with open('nuevo_archivo.csv','r', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)