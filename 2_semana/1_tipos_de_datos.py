
# print('esto sera nuevo en git')



#* TDD PRIMITIVOS EN PY: str, int, float, Bool (True, False).
print('soy primer parametro', 'soy 2do', 'soy 3ro', 4, False, 1.1) #tengo w separa los argumentos con ", " dentro de las funciones


#* VARIABLES: o identificadores: Usa snake_case.
# Etiquetas con las que se ocupa espacios en memoria para guardar el valor asignado, representándolo.
#! Caracteres Prohibidos @, #, $, %, &, *, ( ), [ ], { }, +, =, empezar con numero, espacios.
# La declaracion NO requiere establecer su TDD, dado que PY NO es tipado. El interprete lo entenderá por el valor

userName = 'edi@' #js
user_name = 'edi@' #py

# const PI = 3.14
# let nombre = 'edily'


PI = 3.14 #TDD Floar

#*💡 CONSTANTES: PY NO tiene directiva que impida que un valor sea modificado una vez asignado. 
# Si las usas se recomienda usar mayusculas y guion bajo para identificarlas.
PI = 6 # TDD Int
nombre = 'edily' #TDD Str
auth = True #TDD Bool
auth = False

print(PI, nombre, auth) #esto me imprime el dato, pq estoy llamando a la var que identifica al dato en memoria.

print(type(PI), type(nombre), type(auth), type(10.33)) #aqui vere el TDD de cada dato



#* Metodo para conocer el TDD
# type(valor): Método que Retorna el TDD O Class del valor pasado como parametro.
# <class 'int'> <class 'str'> <class 'bool'> <class 'float'>
print(type('12'))
print(type(12))

#* Reasignacion. 
# El valor y el TDD pueden cambiar a lo largo del programa, ya que PY es de tipado dinámico.
nombre = 'Carmen'
nombre = 2000
# int edad = 20
print('************************Metodos Casting***********************')
# #* Metodos Casting: para convertir entre TDD.
# Permiten convertir un valor de un TDD a otro TDD compatible.
sumando_1 = 1
sumando_2 = int('2010')
restado  = sumando_1 + sumando_2 #! TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(restado) #21

# CONCATENACION enter str
sumando_1 = str(1)
sumando_2 = '2010'
restado  = sumando_1 + sumando_2 #! TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(restado) #12010

# esto NO se permite
str_float =  '1.22'
convertido = str_float
#! print(convertido - 2) #! TypeError: unsupported operand type(s) for -: 'str' and 'int'


# esto se permite
str_float =  '1.22'
convertido = str_float
print(convertido * 2) # 1.221.22

print('****'*10, 'estas aprendiendo TDD ', '****'*10,)

#print('***' / 4) #! TypeError: unsupported operand type(s) for /: 'str' and 'int'

#* USO DE CASTING PARA CONCATENAR, Y CREAR STRINGS
num = 0 #int
num = 1
print(num)
num = bool(num)
print(num)
print(type(num))
print(bool(123))
print(bool(''))
print(bool('a'))
print(bool([1]))

# data = request(url)
# bool(data)

# if bool(data) == False:
#     print('no hay data')
# else: print('no hay data', data[0].nombre)

#* USO DEL CASTING PARA REALIZAR OPERACIONES ARITMÉTICAS
# 💡por lo general la data ingresada por el usuario al sistema, es str y ANTES de procesarla debemos convertirla.



#***************************Generalidades de los numbers: pueden ser:
# Positivos o negativos 
# Expresados en potencia con el carácter "e"
# Son operandos en operaciones (aritmético y comparacion).
# Operando: valor o variable que se usa como entrada para un operador. Ej: 44, 44.44, 4.8e3, ...
# Operador: símbolo o palabra que realiza una operación sobre uno o más operandos. Ej: +, _, *, /, >=, ...
 
# ************************* OPERACIONES ARITMÉTICAS CON NÚMEROS 🧮📱
# ? OPERACIONES ARITMÉTICAS: se realizan SOLO entre int y float
# Suma: +, Resta: -,  Multiplicación: *,  División: / (resultado float) 
#* División entera: // (resultado int) 
# Módulo (residuo): % y Potencia: **
a = 10
b = 20
print(b / a)
#* ⚠️Operador de la división entera "//", depende del tipo de dato del dividendo.
print(b // a) #* div ENTERA!!
print(5 // 3) # 1
print(5 / 3) #* div ENTERA!!
print(5 // 3.0) #* 1.0



# ************************* 🔎OPERACION ARITMÉTICA: EL MODULO
# Devuelve el residuo de la división entre dos números. 
# Se expresa como: 10 modulo 4 → 
print(25 % 4) # 1
print(11 % 4) # 3

# como saber si el num es par: si x % 2 == 0 ES PAR, si da == 1 IMPAR
print('ES PAR?')
print(100 % 2)

print(3 % 4) #3


# ************************* OPERACIONES "ARITMÉTICAS" CON STRINGS
#? concatenacion: entre str con operador '+' 

#? multiplicacion de los strings: str '*' int


#! El resto de operaciones aritmeticas entre str y int/float no son posibles

#💡Haz casting para realizar operaciones, sean aritmeticas o concatenacion



#?*************************Notación Científica “E”
# Expresion resumida de una cifra numérica, con su exponente en base 10. 
# E || e El valor se guardará como TDD float.
# ®️ 2.5e3 = “2.5 multiplicado por 10 a la 3” =  2.5 × 10^3 = 2.5 * 1000 = 2500.0 
entera = 2500
entra_resul = 2.5*1000
entra_nota = -2.5e-3
entra_nota = -2.5E-3
print('notacion cs')
print(entera, entra_resul, entra_nota )


#? ➕E Positiva: El punto se mueve los dígitos E a la derecha y agregas 0 si es necesario.



#? ➖E Negativa: El punto se mueve los dígitos E a la izquierda y agregas 0 si es necesario.



#* Propiedades de las Potencias
# base con exponente positivo, se multiplica por sí mismo tantas veces como indique el exponente.
print(5**1)
print(5**0)
print(0**0) # 👀 1

# REGLA: base con exponente 0, el resultado es 1


#EXCEPCION:💡 base y exponente es 0, es una indeterminacion, pero en contextos discretos como 
# álgebra o programación se define convencionalmente como 1 


import math
# Observa que math.pow devuelve float.


# El exponente negativo indica el inverso multiplicativo de la base elevada al exponente positivo.  

# La base negativa con exponente par da como resultado un número positivo


# La base negativa con exponente impar da como resultado un número negativo 


#TODO: 2_op_asignacion.py






#&FIN DE 1_datosy_tipos_op_aritm.py