# 15. Elaborar un programa en Python que permita para n vehículos, leer la distancia recorrida (en km) y el tiempo de desplazamiento (en horas), calcular la velocidad y determinar:

# -Cuantos de los conductores son infractores, exceden la velocidad máxima permitida de 80 km/h.
# -Calcular el promedio de velocidad de los infractores
# -Determinar la máxima velocidad detectada

# -Nota: El programa termina cuando se digita una distancia de 0 km

total_vehiculos = 0 # Contador para sumar el total de vehículos
infractores = 0 #Contador para infractores
max_velocidad = 0 #Contador para guardar la velocidad máxima
suma_vel_infractores = 0 #Contador para la velocidades de infractores para el promedio 

print("Digite 0 para salir del programa")
while True:
    distancia = float(input("Ingrese la distancia en kilometros: ")) #Se solicita la distancia al usuario
    if distancia == 0: # Si se dígita 0 se rompe el bucle
        break

    tiempo = float(input("Ingrese el tiempo de desplazamiento en (Horas): ")) # Se solicita el tiempo

    velocidad = distancia / tiempo # Se calcula la velocidad 
    print(f"Velocidad: {velocidad:.2f} km/h\n") #Se imprime la velocidad con 2 decimales si hay

    total_vehiculos += 1 # Se suma un vehículo para la iteración

    if velocidad > 80: #Si la velocidad es mayor a 80 se suma un infractor 
        infractores += 1
        suma_vel_infractores += velocidad # Se guarda la velocidad en la variable suma_vel_infractores para poder hacer el promedio 

    if velocidad > max_velocidad: # se está preguntando si la velocidad es mayor que la velocidad máxima registrada hasta ese momento, si sí es mayor, entonces esta va a hacer la nueva velocidad máxima, entonces se actualiza el valor de max_velocidad con ese nuevo dato
        max_velocidad = velocidad

print(f'Total de vehiculos: {total_vehiculos}\n') #Imprime el total de vehiculos registrados 
print(f'Cantidad de infractores: {infractores}\n') # La cantidad de infractores

if infractores > 0: #Si hay al menos 1 infractor 
    promedio_infractores = suma_vel_infractores / infractores # Hace el promedio con el contador de la suma de velocidad de infractores y la divide por la cantidad de infractores
    print (f'El promedio de de la velocidad de los infractores es : {promedio_infractores:.2f} km/h') #Imprime el promedio con dos decimales
else:
    print("No hubo infractores.") #Si no pues imprime que no hubo

print(f'Velocidad máxima detectada: {max_velocidad:.2f} km/h') # Imprime la velocidad máxima