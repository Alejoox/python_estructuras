#13. Cree un programa en Python que permita leer la categoría de afiliación a la EPS para n usuarios y muestre al usuario el valor de la Cuota Moderadora. 
# Al finalizar, el programa debe imprimir el número total de usuarios por cada categoría y el monto total recibido por concepto de cuotas moderadoras.

# Nota: El programa termina cuando se digita el carácter x

# Diccionario con categorías y sus cuotas
cuotas = {
    "A": 3500,
    "B": 11500,
    "C": 20000
}
# Crear dos variables en 0 para poder sumar el total de usuarios por categoría y el total recaudado 
total_usuarios = 0
total_recaudo = 0

# Hacer dos diccionarios iguales para poder hacer el contador de cada usuario y el recaudo 
usuarios_por_categoria = {"A": 0, "B": 0, "C": 0}
recaudo_por_categoria = {"A": 0, "B": 0, "C": 0}

#Se inicia el bucle
while True:
    categoria = input("Ingrese la categoría del usuario (A, B, C) o X para salir: \n").strip().upper() # Se solicita al usuario el tipo de categoría donde puede colocar minusculas o mayusculas y que no hayan espacios en blanco
    
    if categoria == "X": # Si ingresa X termina el bucle
        break
    
    if categoria in cuotas: # Condicion que de acuerdo a lo que ingresa el usuario, busca en el diccionario de cuotas
        cuota = cuotas[categoria] # Por cada vez que ingresa una categoria lo guarda en una variable cuota donde es igual buscar esa categoria en  el diccionario
        usuarios_por_categoria[categoria] += 1 # De acuerdo a la categoría se suma un usuario a esa categoría y se guarda en esa categoría
        recaudo_por_categoria[categoria] += cuota # Es el mismo caso de arriba solo que en vez de sumar uno, empieza a sumar el valor de la categoría 
        print(f"\n El valor de la cuota moderadora para categoría {categoria} es: ${cuota:,.0f}") #Imprime cuanto vale la cuota que ingreso el usuario
    else: # Si no está la categoría imprime el siguiente mensaje
        print("Categoría inválida. Intente de nuevo.")

#Se crea un for por cada vez que se ingrese una categoria y se busca el resultado en el diccionario
for categoria in cuotas:
    cantidad = usuarios_por_categoria[categoria] # Se crea una variable para contar la cantidad de usuarios por categoria
    recaudo = recaudo_por_categoria[categoria] #Lo mismo para la recaudación 
    total_usuarios += cantidad # Se suma todos los usuarios 
    total_recaudo += recaudo # Se suma el total recaudado 
    print(f"Categoría {categoria} - Usuarios: {cantidad}, Total recaudado: ${recaudo:,.0f}") #Imprime Cual es la categoría, la cantidad de usuarios y el recaudo por esa categoría

print(f"\nTOTAL DE USUARIOS: {total_usuarios}") #Imprime el total de todos los usuarios 
print(f"TOTAL RECAUDADO GENERAL: ${total_recaudo:,.0f}") # Imprime el total de recaudación

