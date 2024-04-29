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