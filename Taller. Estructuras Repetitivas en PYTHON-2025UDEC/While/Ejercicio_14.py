#14. COLDEPORTES está interesado en promover el Voleyball y para ello desea vincular a su liga, deportistas que cumplan con las siguientes características:

# -Estatura superior a 1.80
# -Peso inferior a 90 kilos
# -Hacer restricción para magnitudes negativas

# Crear un programa que lea la talla y el peso de los aspirantes y determinar el número de deportistas que cumple con los requerimientos para pertenecer a la liga y su porcentaje con relación al total de aspirantes. 
# El programa termina cuando se digite como dato de estatura el valor cero (0)

total_personas =  0 #Contador para sumar el total de aspirantes
aptos = 0 #Contador para personas aptas

while True:
    estatura = float(input("Ingrese su estatura o (Ingrese 0 para finalizar): ")) #Se le pide la estatura del aspirante

    if estatura == 0: # Si es cero se rompe el bucle
        break
    
    if estatura < 0: # Si es menor a cero impresa este mensaje
        print("La estatura no puede ser negativa. Intente de nuevo.\n")
        continue # Se utiliza la palabra reservada para que siga ejecutandose el bucle, si se cumple

    peso = float(input("Ingrese el peso (en kilogramos): ")) #Se solicita el peso
    if peso < 0: #Se pone la condición de arriba 
        print("El peso no puede ser negativo. Intente de nuevo.\n")
        continue
    total_personas += 1 #Si no cumple ninguna de las condiciones anteriores se suma el total de aspirantes

    if estatura > 1.80 and peso < 90: # Si cumple las condiciones para ser apto entonces se suma uno a personas aptos
        aptos += 1

if total_personas > 0: # Si hay aspirantes se ejecuta la siguiente condición 
    porcentaje = (aptos / total_personas) * 100 # Se crea el porcentaje que es igual a las personas aptas divididas con el total de aspirantes y se multiplica por 100, esto es una regla de tres 
    print(f"Total de aspirantes evaluados: {total_personas}") #Se imprime el total de aspirantes 
    print(f"Número de deportistas aptos: {aptos}") #Total de personas aptas
    print(f"Porcentaje de aptos: {porcentaje:.2f}%") #Y el porcentaje con 2 decimales
else:
    print("\nNo se evaluó ningún aspirante.") # Si no hay aspirantes entonces se imprime que no hubo ninguno
    
    

