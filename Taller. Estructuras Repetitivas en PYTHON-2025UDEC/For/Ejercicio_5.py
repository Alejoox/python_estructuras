# 5. Elaborar un programa que desea calcular el monto total de venta.
# Se deben leer dos variables (costo unitario y cantidad vendida). 
# Imprimir el valor de cada venta y determinar el valor final de la venta si se realizan 10 ventas al día. 
# Validar que no se registren ventas ni cantidades negativas

monto_total = 0 # Se inicia un variable en cero para poder sumar la venta total del día
for i in range(10): # Utiliza un for por iteración con un rango hasta 10 

    cantidad = int(input(f"Ingrese la cantidad vendida del producto #{i+1}: "))  #Se solicita al usuario la cantidad ventida
    if cantidad <= 0: # Una condición para validar que no sea negativo 
        print("La cantidad no puede ser negativa. Intente de nuevo. \n")
        break # Si es menor a cero hay que iniciar de nuevo el problema 

    valor_uni = float(input(f"Ingrese el precio unitario del producto #{i+1}: $")) #Se solicita al usuario el precio unitario
    if valor_uni <= 0: #Igual que en la condición anterior solo que con el valor unitario 
        print("El valor no puede ser negativo. Intente de nuevo. \n")
        break

    monto_venta = valor_uni * cantidad # Una vez que que valide si no hay cantidades, ni valores negativos el monto de venta es el valor unitario multiplicado por la cantidad de cada producto
    print(f"Valor de la venta #{i+1}: ${monto_venta:.2f}") #Imprime el valor

    monto_total += monto_venta # El monto total es para ir acumulando el monto de cada venta, sumandose entre sí hasta que se cumpla el for 
print(f'Monto total de ventas es: ${monto_total:.2f}') # Imprime el resultado y la indentanción no es con el monto por que solo mostraría la suma de un solo producto





    