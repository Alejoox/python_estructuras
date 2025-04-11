#1. Elaborar un programa en Python en Google Colab que imprima una tabla de multiplicar hasta el 10, dado el número multiplicando digitado por teclado

i = int(input("Ingresar un número: ")) #Pedir al usuario que ingrese un número int, el cual va a hacer el que se multiplique 10 veces

for m in range(0,11): #Utilizar range, para poner el límite inferior y superior
    multiplicacion = i * m #Dentro del for hacer declarar una variable la cual es multiplicacion que es para generar que i se multiplique por el rango que hemos asignado
    
    print(f' {m} x {i}  = {multiplicacion}') #Acá se imprime el resultado donde f es una forma de combinar texto con variables, donde muestra los numeros desde el rango multiplicado por i
