# modulos 
import os 
from listas import *
from calculadora import *
from conversor_longitudes import *

# INICIO DEL PROGRAMA
os.system("cls")

# lista de opciones
lista_de_opciones = [
    "Calculadora",
    "Conversor Monedas",
    "Opción 3",
    "Opción 4",
    "Opción 5",
    "Opción 6",
    "Opción 7",
    "Opción 8",
    "Opción 9",
    "Salir"
]

while True:
    cargar_opciones(lista_de_opciones)

    try:  
        respuesta = input("[?] ")

        if respuesta == "1":
            programa_calculadora()
        elif respuesta == "2":
            conversion_monedas()
        elif respuesta == "10":
            break
    
    except:  # SI HAY ERROR
        print("valor nulo")