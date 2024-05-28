#Sumar función que requiere de dos parametros
#@return Retorna el resultado de la operación
#num1+num2

def sumar_num(num1, num2):
    return num1+num2
resultado= sumar_num(10,5)
print(resultado)

def restar(a, b):
    return a - b
resultador = restar(3,2)
print(resultador)

def multiplicacion (a, b):
    return a * b
resultadom = multiplicacion(5, 5)
print(resultadom)

def division (a, b):
    return a/b
resultadod = division(50, 5)
print(resultadod)

#PROGRAMA CALCULADORA
def programa_calculadora():
    print("[1]---------------------------------------")
    print("[1] Multiplicar [2] Dividir")
    print("[3] Sumar       [4] Restar\n")
