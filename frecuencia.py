#Creamos la función y le damos un argumento que es una lista de diccionarios
def grafica_frecuencias(lista):
    #Usamos el bucle for para iterar sobre cada elemento en lista
    for p in lista:
        #Imprimimos el valor de producto de la lista de diccionario, evitamos un salto de línea
        print(p["producto"]," ", end="")
        #Usamos el bucle for para iterar el valor "f" de la lista
        for f in range (p["f"]):
        #Imprime el valor 0 y evita nuevamente el salto de línea
            print("0", end="")
        #Imprime un salto de línea
        print("")
        