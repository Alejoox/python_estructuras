#4. Elaborar un programa en Python que lea n números digitados por teclado
#calcule la suma, el promedio, elvalor máximo y el valor mínimo.

n = int(input("Digite la cantidad de números: ")) # Se le pide al usuario la cantidad de numeros 
numeros = [] # Se hace una lista vacía donde se van a guardar los números 
suma = 0 # se crea una variable para poder sumar los números y que se guarde en esa misma variable

for i in range(n): #Por cada iteración en el rango que colocá el usuario se hace lo siguiente:
    numero = float(input(f"Ingrese el número {i+1}: ")) #Una variable donde se le pide al usuario un número y de acuerdo a cada iteración pide un número
    numeros.append(numero) # Append sirve para agregar items, en este caso a la lista vacía
    suma += numero # se hace la respectiva suma donde se suma la misma variable con los números
    promedio = suma / n #Se hace el promedio de el valor de la suma entre la cantidad de números que hay 
#Se imprimen los resultados, junto con el máximo y el mínimo término, gracias a una palabra reservada
print("Los números son:", numeros)
print("La suma total es: ", suma)
print("El promedio es de: ", promedio)
print("El valor máximo es: ", max(numeros))
print("El valor mínimo es: ", min(numeros))


    