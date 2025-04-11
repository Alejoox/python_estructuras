# 9. Elaborar un programa en Python que permita matricular m estudiantes de los diferentes programas académicos diferentes, según la siguiente tabla:
#Al finalizar el programa se debe mostrar:

#- Número de estudiantes matriculados por programa académico
#- Total, recaudado por cada programa académico
#- Total, recaudado por concepto de todas las matrículas

# Se hace un diccionario donde el codigo guarda el nombre de la carrera y el valor 
programas_academicos = {"ICI":{"Nombre":"Ing.civil","Valor":55410000},
    "ZT":{"Nombre":"Zootecnia","Valor":5161000},
    "IMC":{"Nombre":"Ing. Mecatrónica","Valor":5451000},
    "IIN":{"Nombre":"Ing. Ing. Industrial","Valor":5491000},
    "IAM":{"Nombre":"Ing. Ing. Ambiental","Valor":5349000},
    "PD":{"Nombre":"Derecho","Valor":5006000},
    "IAL":{"Nombre":"Ing. de alimentos","Valor":5464000}}

estudiantes = {codigo:0 for codigo in programas_academicos} # Se inician dos variables para guardar los estudiantes 
recaudo_programa = {codigo:0 for codigo in programas_academicos}

matriculación = int(input("Ingrese la cantidad de estudiantes a matricular: "))
for i in range (matriculación):
    codigo = input("Ingrese el código del programa (ICI, ZT, IMC, IIN, IAM, PD, IAL): ").strip().upper()
    
    if codigo in programas_academicos:
        estudiantes[codigo] += 1
        recaudo_programa[codigo] += programas_academicos[codigo]["Valor"]
    else:
        print("Código no de programa no válido. Estudiante no matriculado")
total = 0
for codigo in programas_academicos: 
    nombre = programas_academicos[codigo]["Nombre"]
    cantidad = estudiantes[codigo]
    recaudo = recaudo_programa[codigo]
    total += recaudo
    print(f'{nombre}({codigo}-Estudiantes: {cantidad}, Recaudado:{recaudo:,.0f}')
print("Total de recaudación por el total de las matriculas es: $", total)

