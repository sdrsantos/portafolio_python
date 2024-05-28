import os


#Importar funciones
from listas import cargar_opciones
from calculadora import programa_calculadora

#Limpiar terminal
os.system("cls")

#Llamar a la función
cargar_opciones()

#EJECUTO EL PROGRAMA ESPERANDO UN POSIBLE ERROR
try: #SI NO HAY ERRORES
    respuesta = input("[?]")
    if respuesta == "1":
        programa_calculadora()
except: #SI HAY ERROR
    print("valor nulo")