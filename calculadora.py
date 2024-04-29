import math
from constants import *
    

def is_number(num, return_number = False): #funcion para verificar que sea un numero
    try: #si no es un numero entero, intenta convertirlo a decimal
        num = int(num)
    except ValueError:
        try: #si no es un numero decimal, imprime un error
            num = float(num)
        except ValueError:
            return False
        
    if return_number:#si se necesita el numero, lo devuelve por defecto es False
        return num
    
    return is_number



def contar_parentesis(expresion,tipo): #funcion para contar los parentesis
    parentesis = 0
    if tipo == "abiertos":
        parentesis_type = "("
    if tipo == "cerrados":
        parentesis_type = ")"

    for letra in expresion:
        if letra == parentesis_type:
            parentesis += 1
    return parentesis



def validar_parentesis(expresion): #funcion para verificar que los parentesis esten bien
    parentesis_abiertos = 0
    parentesis_cerrados = 0
    
    for letra in expresion: #recorre la expresion y cuenta los parentesis hasta que sean iguales o hasta que se termine la expresion
        if letra == "(":
            parentesis_abiertos += 1
        if letra == ")":
            parentesis_cerrados += 1
        if parentesis_abiertos == parentesis_cerrados: 
            break

    parentesis_error = "Los parentesis no se utilizan correctamente"

    if parentesis_abiertos > parentesis_cerrados:
        ERROR(parentesis_error)
        return False

    if parentesis_abiertos < contar_parentesis(expresion,"cerrados"):
        ERROR(parentesis_error)
        return False
    
    if contar_parentesis(expresion,"abiertos") > parentesis_abiertos:
        ERROR(parentesis_error)
        return False
    
    if contar_parentesis(expresion,"cerrados") > parentesis_cerrados:
        ERROR(parentesis_error)
        return False
    return True


def operador_valido(operador): #funcion para verificar que el operador sea valido
    operador = operador.replace("(", "")
    lista_operaciones = ["+","-","*","/","^","sqroot","sqr","sin","cos","tan","div","%","!"]
    if operador not in lista_operaciones or operador == "":
        return False
    return True


def one_number_operation(operador,num=None): #funcion para operaciones con un solo numero
    if operador == "sqroot":
        if num < 0:
            ERROR("No se puede sacar la raiz cuadrada de un numero negativo")
            return
        return(math.sqrt(num))
    if operador == "sqr":
        return(num**2)
    if operador == "sin":
        return(math.sin(num))
    if operador == "cos":
        return(math.cos(num))
    if operador == "tan":
        return(math.tan(num))
    if operador == "!":
        pass
    
def two_number_operation(operador,num1=None, num2=None): #funcion para operaciones con dos numeros
    #errores de division
    if num2 == 0 and (operador == "/" or operador == "div" or operador == "%"):
        ERROR("Division entre 0")
        return False

    if operador == "+":
        return(num1+num2)
    if operador == "-":
        return(num1-num2)
    if operador == "*":
        return(num1*num2)
    if operador == "/":
        return(num1/num2)
    if operador == "div":
        pass
    if operador == "%":
        pass
    

  


def operar(operador,expresion): #funcion para calcular la operacion
    numbers = []
    for number in expresion:
        if not is_number(number):
            ERROR(f'"{number}" no es un numero')
            return False
        else:
            numbers.append(is_number(number, True)) 

    if len(numbers) == 1:
        return one_number_operation(operador,numbers[0])
    elif len(numbers)>1:
        return two_number_operation(operador,numbers[0],numbers[1])
    else:
        ERROR("No se ingresaron suficientes numeros")
        return False



def evaluar_expresion(expresion): #funcion para evaluar la expresion
    lista_expresion = expresion.split(" ") #separa la expresion en una lista
    if not operador_valido(lista_expresion[0]):
        ERROR("Operador no valido")
        return

    #operacion simple
    if contar_parentesis(expresion,"abiertos") == 1 and operador_valido(lista_expresion[0]): 
        operador = lista_expresion[0].replace("(", "")#se obtiene el operador
        lista_expresion[-1] = lista_expresion[-1].replace(")", "")#se obtiene el segundo numero sin parentesis
        res = operar(operador,lista_expresion[1:])
        return (res)
    

    elif contar_parentesis(expresion,"abiertos") > 1:
        cantidad_parentesis = contar_parentesis(expresion,"abiertos")
        temp_results = []
        for i in range(cantidad_parentesis,0,-1):
            print('expresion',expresion)
            temp_expression = ""
            contador = 0
            for letra in expresion:
                if letra == "(":
                    contador += 1
                if contador == i:
                    temp_expression += letra
                    if letra == ")":
                        temp_results.append(evaluar_expresion(temp_expression))
                        expresion = expresion.replace(temp_expression,str(temp_results[-1]))#se reemplaza la expresion por el resultado
                        break

        return temp_results[-1] #se devuelve el resultado de la ultima operacion




def calculator(calc_input): #funcion principal de la calculadora

    if calc_input == "quit": #salir del programa
        print(BYE)
        exit()
    if calc_input == "help":
        print(HELP)
        return
    if calc_input == "":
        ERROR("No se ingreso ninguna expresion")
        return
    
    if(validar_parentesis(calc_input)): #verificar los parentesis   
        if calc_input[0]=="(" and calc_input[-1]==")": #se verifica si es una expresion y se evalua
            RESULT(evaluar_expresion(calc_input))

        elif (calc_input[0]!="(") and (calc_input[-1]!=")"):#si no tiene parentesis verifica si es numero y lo devuleve
            if not is_number(calc_input): 
                ERROR()
            else:
                RESULT(calc_input)
        else:
            ERROR()
                



def main():
    print(WELCOME)
    while True:  #ciclo principal
        calc_input = input("TextCalc >> ")
        calculator(calc_input) #llama a la funcion calculator con el input del usuario

main()            