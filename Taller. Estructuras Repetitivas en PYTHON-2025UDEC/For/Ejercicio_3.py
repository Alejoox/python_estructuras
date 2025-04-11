#3. Elaborar un programa en Python que cuente los números naturales impares menores de 100.

i = int # Se inicia una variable donde el tipo de dato es entero
for i in range(100): # i es la iteración en un rango de números hasta 100
    if i%2 == 1: #se coloca la condición de que si el residuo del número divido en 2 es uno, entonces es un número impar
        print (i) # Se imprime i