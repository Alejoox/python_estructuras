#12. Una compañía debe calcular la comisión que reciben los vendedores de su departamento de ventas teniendo en cuenta el valor mensual de ventas de cada uno (valor de venta ingresado por teclado). 
# Las comisiones se calculan así:

# -Ventas menores de $4.000.000 el 3%
# -Ventas entre $4.000.000 y $10.000.000 el 5%
# -Ventas Mayores que $10.000.000 hasta $20.000.000 el 10%
# -Ventas superiores a $20.000.000 el 15%

# Realizar un programa en Python que muestre para cada vendedor el valor total de las ventas y la comisión correspondiente.
# El programa termina cuando se digita como valor de ventas el número cero (0)

suma_ventas = 0 #Se inicia una variable en cero, para poder sumar cada venta

while True: #Se crea el bucle con valor True para que se haga infinito
    ventas = float(input("Ingrese el valor de ventas del vendedor (0 para salir): ")) #Se piden las ventas, y para acabar con el bucle se digita 0

    if ventas == 0: # condicional de que si es igual a 0 imprime un mensaje y rompe el bucle
        print("Nos vemos el otro mes")
        break
    suma_ventas += ventas #En la variable cada vez que se ingresen ventas se van sumando y se guardan en esa variable
    
    #Se utilizan condicionales para comparar las ventas y calcular la comision
    if ventas < 4000000: 
        comision = ventas * 0.03
        porcentaje = 3

    elif 4000000 > ventas < 10000000: # Se utilizan elif para que si no cumple la antenrior condición, entonces se crea otra condición hasta que recorre todas las opciones posibles
        comision = ventas * 0.05
        porcentaje = 5
    
    elif 10000000 > ventas < 20000000:
        comision = ventas * 0.10
        porcentaje = 10
        
    elif ventas > 20000000:
        comision = ventas * 0.15
        porcentaje = 15

print(f'El valor de total de las ventas fue: ${suma_ventas:,.0f}') #Imprime el total de ventas por el vendedor y se coloca .0f para 0 decimales + coma de miles
print(f'La comisión correspondiente fue: ({porcentaje}%): ${comision:,.0f}') #Imprime el porcenta y de cuanto fue la comisión con 0 decimales + coma de miles
