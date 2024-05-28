#Sumar función que requiere de dos parametros
#@return Retorna el resultado de la operación
#num1+num2

def sumar_num(num1, num2):
    return num1+num2

def restar(a, b):
    return a - b

def multiplicacion (a, b):
    return a * b

def division (a, b):
    return a/b

#PROGRAMA CALCULADORA
def programa_calculadora():
    print("[1]---------------------------------------")
    print("[1] Multiplicar [2] Dividir")
    print("[3] Sumar       [4] Restar\n")

    opcion = input("[?]: ")

    num1 = int(input("[Num 1]: "))
    num2 = int(input("[Num 2]: "))

    if opcion == '1':
        print("[R]: ", multiplicacion(num1,num2)) 
    elif opcion == '2':
        print("[R]: ", division(num1, num2))
    elif opcion == '3':
        print("[R]: ", sumar_num(num1, num2))
    elif opcion == '4':
        print("[R]: ", restar(num1, num2))

    print("--------------------------------")