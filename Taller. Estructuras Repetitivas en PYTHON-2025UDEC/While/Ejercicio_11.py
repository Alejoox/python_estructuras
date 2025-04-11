#11. Leer la temperatura de los pacientes de una clínica atendidos por COVID-19 durante un turno de enfermería y elaborar un programa en PYTHON que calcule e imprima:

# -Promedio de temperaturas
# -Máxima temperatura
# -Mínima temperatura

# Si presentan una temperatura superior de 37.8 °C, indica que los pacientes están afiebrados. Contar e imprimir cuantos pacientes están en esta situación.
# Nota: El número máximo de pacientes atendidos por turno debe ser 12.

temperaturas = [] #Crear una lista vacía donde guardar el total de temperaturas
temperaturas_altas = [] #Crear otra lista vacía para guardad a pacientes con temperaturas > 37.8 °C
suma_temperaturas = 0 #Iniciar una variable en cero para poder sumarse con las diferentes temperaturas
pacientes = 0 #Iniciar está variable en cero para poder sumar la cantidad de pacientes que hay 

inicio_turno = str(input("Nuevo turno? (Si/No): ").upper())# Preguntar si va a haber un nuevo turno 

if inicio_turno == "si": #Se utiliza un if porque si hay un while queda un bucle infinito y el ejercicio es hasta 12
    
    while pacientes < 12: #Un bucle while donde se pregunta la temperatura hasta que sea menor a 12

        temperatura = float(input(f"Ingrese la temperatura del paciente en grados Celsius: ")) #Solicita la temperatura
        temperaturas.append(temperatura) # Agrega las temperaturas a la lista
        suma_temperaturas += temperatura # Suma la variable + las temperaturas ingresadas

        if temperatura > 37.8: # Se agrega una condición donde si es mayor a 37.8 entonces 
            temperaturas_altas.append(temperatura) #se agrega el valor en la lista de temperaturas altas

        pacientes += 1 #Se suma uno al paciente y se repite el ciclo hasta llegar al límite

        #Cuando llega al límite se hace lo siguiente:
        promedio_temperaturas = suma_temperaturas / {len(temperaturas)} # Hacer el promedio de la suma dividido entre la cantidad de temperaturas por se se utiliza len
        #Se imprime lo solicitado por el ejercicio 
        print(f"El promedio de temperaturas fue: {promedio_temperaturas}°C\n")
        print(f"Pacientes con fiebre temperaturas mayor a 37.8 °C): {len(temperaturas_altas)}\n")
        print(f"La temperatura máxima fue: {max(temperaturas)} °C")
        print(f"La temperatura mínima fue: {min(temperaturas)} °C\n")
        print("Nos vemos mañana 😁")
else:
    print("No se inició ningún turno.") # Si el usuario coloca que no, no se hace el bucle


    
    