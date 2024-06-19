# modulos 
import os 
from listas import *
from calculadora import *
from conversor_longitudes import *
from frecuencia import *

# INICIO DEL PROGRAMA
os.system("cls")

# lista de opciones
lista_de_opciones = [
    "Calculadora",
    "Conversor de Monedas",
    "Gráfica de frecuencias",
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
        elif respuesta == "3":
            lista = [
                {"producto":"Tomate   ", "f":20},
                {"producto":"Coliflor ", "f":30},
                {"producto":"Espinaca ", "f":25},
                {"producto":"Apio     ", "f":35},
                ]
            grafica_frecuencias(lista)
        elif respuesta == "10":
            break
    
    except:  # SI HAY ERROR
        print("valor nulo")