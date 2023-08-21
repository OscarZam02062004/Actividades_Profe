#desarrollar un programa  con un menu iterativo que contenga dos funciones 
#embebidas,la primera debera calcular Req en serie y la segunda 
#por lo tanto el usuario debe elegir la opcion y dar el resultado
# Tarea: preguntarle al usuario si desea añadir otra resistencia o no
resistencias=[]
def menu():
    op="0"
    while True:
        op=input("Ingresa 1 para  circuito en serie, 2 para circuito en paralelo: ")
        if op=="1":
            serie()
            break
        if op=="2":
            paralelo()
            break
        else:
            print("Elije un opcion valida")
def serie():
#Se crea un for en el que se le va indicar cuantas resistencias quiere
    cantidad_resistencias = int(input("Por favor, ingresa la cantidad de resistencias que deseas añadir: "))
    for i in range(cantidad_resistencias):
        valor=float(input(f"Ingrese el valor de la resistencia {i+1}:"))
#Se crea una lista vacia en donde se guardaran todas las resistencias
        resistencias.append(valor)
#Se utiliza la funcion sum para sumar los valores de una lista
        req=sum(resistencias)
    print(f"La resistencia equivalente es: {req}")
def paralelo():
    cantidad_resistencias=int(input("Ingresa la cantidad de resitencias que deseas añadir: "))
    for i in range(cantidad_resistencias):
        valor=float(input(f"Ingresa el valor de la resistencia {i+1}:"))
        resistencias.append(valor)
#La operacion en paralelo se crea un for dentro de la operación
#en el que sumara todos los valores de las resistencias de cada dato dividido en 1
        req=1/sum(1/r for r in resistencias)
    print(f"La resistencia equivalente es: {req}")

menu()

