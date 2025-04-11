# 6. Realizar un programa que imprima los 25 primeros términos de la serie 11, 22, 33, 44, etc.
#(No se ingresan valores por teclado)

for i in range(25): #Se utiliza un for que haya una iteración en un rango de 25 números
    serie = i * 11 #Se hace una variable, donde cada iteración se multiplica por 11 que es la progresión, si se quisiera elegir desde donde inicia, entonces se sumaría con el resultado de la multiplicación

    print(serie)#Se indenta el print porque no haría correctamente el ciclo y estaría mostrando el último valor y no la progesión
    
