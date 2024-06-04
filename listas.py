#Lista
lista_de_opciones = [
    "Calculadora", 
    "Opción 2", 
    "Opción 3", 
    "Opción 4", 
    "Opción 5", 
    "Opción 6", 
    "Opción 7", 
    "Opción 8", 
    "Opción 9", 
    "Salir" 
]

def cargar_opciones():
    print("-"*30)
    for opcion in lista_de_opciones:
        indice = lista_de_opciones.index(opcion)+1
        if indice %2 == 0:
            print(f"[{indice}] {opcion}")
        else:
            mensaje = f"[{indice}]{opcion}"
            print(f"[{indice}] {opcion}"," "*(14-len(mensaje)),end=" ")
    print("\n", "-"*29)