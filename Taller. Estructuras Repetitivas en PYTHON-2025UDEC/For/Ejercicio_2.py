#2.Elaborar un programa en Python que permita leer el valor de x y resolver la función:
#f(x) = (2x- 1)³-(x -4)²-4x-5
#para x con valores desde 0 hasta 10 en incrementos de 1

for x in range(0,11,+1): #Se utiliza for en cada iteración de x donde empieza desde 1, hasta 11 con incremento de 1
    oper1 = (2 * x - 1)**3 #Se divide la función en 4 operaciones, cada una tiene su nombre correspondiente aca se multiplica el 2 por x osea la iteración -1, y después se eleva al cubo
    oper2 = (x - 4)**2 #Esta operacion se resta x menos 4 y el resultado se eleva al cuadrado 
    oper3 = 4 * x #4 se multiplica por x 
    resultado = oper1 - oper2 - oper3 - 5 # Después de todas las operaciones se restan entre sí y el 5 
    print(f'f({x}) = {resultado}') # Se imprime el resultado donde f en morado es para poder combinar texto con operaciones e imprime f(x) = al resultado donde x es la iteración