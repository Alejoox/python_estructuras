#8.Realizar un programa para calcular el precio total de cada uno de los n-artículos de una compra,
#dado el precio y sabiendo que el descuento es del 10% si el precio es menor a $50.000, en caso contrario el descuento es del 
#15%. Calcular y escribir además la suma de los precios totales superiores a $100.000 y la suma de los precios totales menores o iguales a $100.000

articulos = int(input("Ingrese la cantidad de artículos: "))  #Se solicita la cantidad de artículos a verificar el precio
suma_mayor_100 = 0 # Un contador para la suma mayor a $100.000
suma_menor_100 = 0 # Un contador para la suma menor a $100.000

for i in range(articulos): # Se hace una interacion donde el rango son la cantidad de artículos ingresados por el usuario
    precio = float(input(f"\n Ingrese el valor del artículo #{i+1}: $")) # Se solicita el valor del artículo

    if precio < 50000: # Condición de que si es menor a $50.000 
        descuento = precio * 0.10 # Se hace un descuento del 10%
        porcentaje = 10
    else: #Si no, entonces
        descuento = precio * 0.15 # Se hacer del 15%
        porcentaje = 15

    total = precio - descuento # se hace el total que es donde se le resta el descuento al precio
    print(f"El descuento fue es de {porcentaje}%") #Se imprime el porcentaje de descuento correspondiente 
    print(f"Descuento aplicado: $ {descuento:,.0f}") #Se imprime cuanto fue el descuento
    print(f"Precio total con descuento: ${total:,.0f}\n") #Se imprime cual fue el precio total con descuento
    
    if total >= 100: # Una condición para la suma de los precios menores a $100.000
        suma_menor_100 += total
    else: # Si es mayor, entonces se suma a la variable de suma mayor a 100
        suma_mayor_100 += total

#Se imprimen los resultados de las sumas
print(f"Los precios mayores a $100.000 fueron: ${suma_mayor_100:,.0f}") 
print(f"Los precios menores a $100.000 fueron: $ {suma_menor_100:,.0f}")
