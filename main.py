import os


#Importar funciones
from listas import cargar_opciones
from calculadora import programa_calculadora

#Limpiar terminal
os.system("cls")

#Llamar a la función
while True:
    cargar_opciones()
#EJECUTO EL PROGRAMA ESPERANDO UN POSIBLE ERROR
    try: #SI NO HAY ERRORES
        respuesta = input("[?]")
        if respuesta == "1":
            programa_calculadora()
        elif respuesta == "10":
            break
    except: #SI HAY ERROR
        print("valor nulo")