# 7. Elaborar un programa en Python que lea 10 números y determine cuántos son positivos.

numbers_positivos = [] # Se crea una lista vacía para guardar los números positivos 
numbers_negativos = [] # Se crea otra lista para agregar los números negativos
for i in range(10): # Por cada iteración en un rango de 10 
    numeros = float(input(f"Ingrese el número positivo o negativo {i+1}: ")) # Se le pide que ingrese los diez números
    if numeros >= 0: # Se utiliza un if si los números ingresados son mayores o iguales a cero
        numbers_positivos.append(numeros) # Se agregan a la lista de números positivos
    else:#Si no, entonces
        numbers_negativos.append(numeros) # Se agrega a la lista de números negativos
# Se imprimen las listas 
print("Los números positivos son: ", numbers_positivos)
print("Los números negativos fueron: ", numbers_negativos)