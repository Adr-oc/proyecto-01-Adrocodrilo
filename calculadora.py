import math
'''
NOTA IMPORTANTE: en todo el codigo se utilizan colores, \033[ es el codigo de escape de colores en la terminal
tambien utilizamos f-strings para concatenar strings y variables por que creemos que es mas legible asi.
'''

#constantes (para tener el codigo mas limpio y ordenado)
WELCOME = '''
\033[94m 
.————————————( TextCalc )————————————.
| \033[0mBy: Joaquin Gomez & Adrian Orantes\033[94m |
| \033[93m    Ingresa "help" para ayuda\033[94m      |  
'————————————————————————————————————'\033[0m

'''
BYE = "Saliendo...\nGracias por usar TextCalc."
HELP = '''
Para usar esta calculadora, ingresa expresiones en el siguiente formato:

Operaciones válidas:
- Suma: (+ [expresión] [expresión])
- Resta: (- [expresión] [expresión])
- Multiplicación: (* [expresión] [expresión])
- División: (/ [expresión] [expresión])
- Raíz cuadrada: (sqroot [expresión])
- Cuadrado: (sqr [expresión])
- Seno: (sin [expresión])
- Coseno: (cos [expresión])
- Tangente: (tan [expresión])

Formato de expresiones:
- [expresión] puede ser un número entero, decimal o una expresión compuesta entre paréntesis.
- Los números negativos no llevan paréntesis.
- Las expresiones compuestas deben llevar paréntesis.

Ejemplos:
- Suma: (+ 4 5)
- Raíz cuadrada: (sqroot 64)
- Operaciones compuestas: (+ 4 (sqroot 64))

Recuerda que las expresiones deben estar correctamente escritas y en el formato especificado.
'''

def RESULT(expression): #funciones para imprimir los resultados y errores
    print(f"\033[92m  resultado >>\033[0m {expression}")

def ERROR(error = "La sintaxis no es correcta"):#funcion para imprimir errores 
    print(f'\033[91m  ERROR! {error}\033[0m')
    

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
        RESULT(math.sqrt(num))
    if operador == "sqr":
        RESULT(num**2)
    if operador == "sin":
        RESULT(math.sin(num))
    if operador == "cos":
        RESULT(math.cos(num))
    if operador == "tan":
        RESULT(math.tan(num))
    
def two_number_operation(operador,num1=None, num2=None): #funcion para operaciones con dos numeros
    if operador == "+":
        RESULT(num1+num2)
    if operador == "-":
        RESULT(num1-num2)
    if operador == "*":
        RESULT(num1*num2)
    if operador == "/":
        if num2 == 0:
            ERROR("Division entre 0")
            return
        RESULT(num1/num2)

def unique_operation(operador,num1,num2): #funcion para operaciones unicas
    if operador == "div":
        pass
    if operador == "%":
        pass
    if operador == "!":
        pass
     


def operar(operador,expresion): #funcion para calcular la operacion
    print (expresion)
    numbers = []
    for number in expresion:
        if not is_number(number):
            ERROR(f'"{number}" no es un numero')
            return
        else:
            numbers.append(is_number(number, True)) 
    if len(numbers) == 1:
        one_number_operation(operador,numbers[0])
    if len(numbers) == 2:
        two_number_operation(operador,numbers[0],numbers[1])
    if len(numbers) == 3:
        unique_operation(operador,numbers[0],numbers[1],numbers[2])

def evaluar_expresion(expresion): #funcion para evaluar la expresion
    lista_expresion = expresion.split(" ") #separa la expresion en una lista
    if not operador_valido(lista_expresion[0]):
        ERROR("Operador no valido")
        return

    #operacion simple
    if contar_parentesis(expresion,"abiertos") == 1 and operador_valido(lista_expresion[0]): 
        operador = lista_expresion[0].replace("(", "")#se obtiene el operador
        lista_expresion[-1] = lista_expresion[-1].replace(")", "")#se obtiene el segundo numero sin parentesis
        operar(operador,lista_expresion[1:])

    else:
        ERROR("XD")
        return




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
            evaluar_expresion(calc_input)

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