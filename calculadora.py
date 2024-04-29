'''
Autores:
Joaquin Gomez  - 24000172 
Adrian Orantes - 24002878 

NOTA IMPORTANTE: en todo el codigo se utilizan colores, \033[ es el codigo de escape de colores en la terminal
tambien utilizamos f-strings para concatenar strings y variables por que creemos que es mas legible asi.
'''

import math

# naranja = \033[93m 
# azul = \033[94m
# verde = \033[92m
# rojo = \033[91m
# reset = \033[0m

#variables de texto(para tener el codigo mas limpio y ordenado) no utilizo constantes para no utilizar memoria innecesaria
welcome = '''
\033[94m 
.————————————( TextCalc )————————————.
|\033[0m  By: Joaquin Gomez  - 24000172     \033[94m| 
|\033[0m      Adrian Orantes - 24002878     \033[94m|
|\033[93m     "quit" para salir              \033[94m|
|\033[93m     "help" para ayuda              \033[94m|  
'————————————————————————————————————'\033[0m

'''
bye = '''\033[93m
Saliendo...
Gracias por usar TexxtCalc.\033[0m'''
help = '''\033[93mAyuda de TextCalc \033[0m
\033[92mOperaciones validas:\033[0m
Suma: (+ [expresion] [expresion])
Resta: (- [expresion] [expresion])
Multiplicacion: (* [expresion] [expresion])
Division: (/ [expresion] [expresion])
Raiz cuadrada: (sqroot [expresion])
Cuadrado: (sqr [expresion])
Seno: (sin [expresion])
Coseno: (cos [expresion])
Tangente: (tan [expresion])

\033[92mFormato de expresiones:\033[0m
-[expresion] puede ser un numero entero, decimal o una expresion compuesta entre parentesis.
-Los numeros negativos no llevan parentesis.
-Las expresiones compuestas deben llevar parentesis. Operaciones compuestas: (+ 4 (sqroot 64))
-Las expresiones deben estar correctamente escritas
y en el formato especificado
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



def contar_parentesis(expresion, tipo): #funcion para contar los parentesis
    parentesis = 0
    
    if tipo == "abiertos": #cuenta los parentesis abiertos
        parentesis_type = "("
        i = 0
        while i < len(expresion):
            if expresion[i] == parentesis_type:
                parentesis += 1
                while i+1 < len(expresion) and expresion[i+1] == parentesis_type:
                    i += 1
            i += 1
    
    if tipo == "cerrados": #cuenta los parentesis cerrados
        parentesis_type = ")"
        i = len(expresion) - 1
        while i >= 0:
            if expresion[i] == parentesis_type:
                parentesis += 1
                while i-1 >= 0 and expresion[i-1] == parentesis_type:
                    i -= 1
            i -= 1
    
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



def factorial(num): #funcion para calcular el factorial
    if num == 0:
        return 1
    return num * factorial(num-1)



def one_number_operation(operador,num=None): #funcion para operaciones con un solo numero
    #errores de operaciones
    if operador == "sqroot":
        if num < 0:
            ERROR("No se puede sacar la raiz cuadrada de un numero negativo")
            return
        return(math.sqrt(num))
    if operador == "tan" and num == 90:
        ERROR("No se puede calcular la tangente de 90 grados")
        return
    
    #operaciones
    if operador == "sqr":
        return(num**2)
    if operador == "sin":
        return(math.sin(math.radians(num)))
    if operador == "cos":
        return(math.cos(math.radians(num)))
    if operador == "tan":
        return(math.tan(math.radians(num)))
    if operador == "!":
        return factorial(num)



def two_number_operation(operador,num1=None, num2=None): #funcion para operaciones con dos numeros
    #errores de division
    if num2 == 0 and (operador == "/" or operador == "div" or operador == "%"):
        ERROR("Division entre 0")
        return False

    #operaciones
    if operador == "+":
        return(num1+num2)
    if operador == "-":
        return(num1-num2)
    if operador == "*":
        return(num1*num2)
    if operador == "/":
        return(num1/num2)
    if operador == "div":
        return(num1//num2)
    if operador == "%":
        return(num1%num2)
    


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

    #si solo hay un parentesis
    if contar_parentesis(expresion,"abiertos") == 1: 
        if not operador_valido(lista_expresion[0]):
            ERROR("Operador no valido")
            return False
        operador = lista_expresion[0].replace("(", "")#se obtiene el operador
        lista_expresion[-1] = lista_expresion[-1].replace(")", "")#se obtiene el segundo numero sin parentesis
        res = operar(operador,lista_expresion[1:])
        return (res)
    

    elif contar_parentesis(expresion,"abiertos") > 1:
        cantidad_parentesis = contar_parentesis(expresion,"abiertos")
        temp_results = []
        for i in range(cantidad_parentesis,0,-1):
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
    else:
        ERROR("Error al evaluar la expresion")
        return False



def calculator(calc_input): #funcion principal de la calculadora

    if calc_input == "quit": #salir del programa
        print(bye)
        exit()
    if calc_input == "help":
        print(help)
        return
    if calc_input == "":
        ERROR("No se ingreso ninguna expresion")
        return
    
    if(validar_parentesis(calc_input)): #verificar los parentesis   
        if calc_input[0]=="(" and calc_input[-1]==")": #se verifica si es una expresion y se evalua
            resultado = evaluar_expresion(calc_input)
            if resultado:
                RESULT(resultado)
                

        elif (calc_input[0]!="(") and (calc_input[-1]!=")"):#si no tiene parentesis verifica si es numero y lo devuleve
            if not is_number(calc_input): 
                ERROR()
            else:
                RESULT(calc_input)
        else:
            ERROR()
                


def main():
    print(welcome)
    while True:  #ciclo principal
        calc_input = input("TextCalc >> ")
        calculator(calc_input) #llama a la funcion calculator con el input del usuario

main()            