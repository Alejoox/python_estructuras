#10. Desarrollar un programa en Python que permita leer las estaturas de n estudiantes de un colegio y determinar y escribir cuántos están dentro de los siguientes rangos:

# Entre 0,90 m y 1,60 m
# Mayores que 1,60 m y menores que 1,70 m
# Entre 1,70 m y 1,80 m
# Mayores que 1,80 m y menores o iguales a 2,10
# Las estaturas no pueden ser inferiores a 0,90 ni mayores a 2,10


numero_estudiantes = int(input("Ingrese el número de estudiantes: ")) # Se solicita el número de estudiantes a matricular

#Se crean 4 listas vacías para poder almacenar los datos de las personas que se ingresen 
primer_rango = []  
segundo_rango = []
tercer_rango = []
cuarto_rango = []

for i in range(numero_estudiantes): #Se crea un for para el número de estudiantes que ingrese el usuario
    estatura = float(input(f"Ingrese la esturatura del estudiante #{i+1}: ")) # Se solicita la estatura al usuario

    #Se crea la condición de que si es menor a 0.90 y mayor a 2.10 no se permite
    if estatura < 0.90:
        print("La estatura no es válida. Intente de nuevo")
        break
    if estatura > 2.10:
        print("La estatura no es válida. Intente de nuevo")
        break

    if estatura > 0.90 and estatura <= 1.60: # se crean las condiciones donde si se cumplen se agrega el dato a las listas vacías
        primer_rango.append(estatura)
    elif 1.60 <= estatura <= 1.70:
        segundo_rango.append(estatura)
    elif 1.70 > estatura <= 1.80:
        tercer_rango.append(estatura)
    elif 1.80 > estatura <= 2.10:
        cuarto_rango.append(estatura)

#Se imprimen la cantidad de estudiantes de los rangos correspondientes, donde la función len hace eso 
print(f'Estudiantes que están entre 0.90 m y 1.60 m:{len(primer_rango)}\n')
print(f'Estudiantes con altura mayor a 1.60 m y menores a 1.70 m:{len(segundo_rango)}\n')
print(f'Estudiantes con altura entre a 1.70 m y 1.80 m:{len(tercer_rango)}\n')
print(f'Estudiantes con altura mayor a 1.80 m y menores o igual a 2.10 m:{len(cuarto_rango)}')
    