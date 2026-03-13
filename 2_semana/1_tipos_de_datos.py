
#* TDD PRIMITIVOS EN PY: str, int, float, Bool (True, False).



#* VARIABLES: o identificadores: Usa snake_case.
# Etiquetas con las que se ocupa espacios en memoria para guardar el valor asignado, representándolo.
#! Caracteres Prohibidos @, #, $, %, &, *, ( ), [ ], { }, +, =, empezar con numero, espacios.
# La declaracion NO requiere establecer su TDD, dado que PY NO es tipado. El interprete lo entenderá por el valor




#*💡 CONSTANTES: PY NO tiene directiva que impida que un valor sea modificado una vez asignado. 
# Si las usas se recomienda usar mayusculas y guion bajo para identificarlas.


#* Metodo para conocer el TDD
# type(valor): Método que Retorna el TDD O Class del valor pasado como parametro.


#* Reasignacion. 
# El valor y el TDD pueden cambiar a lo largo del programa, ya que PY es de tipado dinámico.



print('************************Metodos Casting***********************')
# #* Metodos Casting: para convertir entre TDD.
# Permiten convertir un valor de un TDD a otro TDD compatible.




#* USO DE CASTING PARA CONCATENAR, Y CREAR STRINGS



#* USO DEL CASTING PARA REALIZAR OPERACIONES ARITMÉTICAS
# 💡por lo general la data ingresada por el usuario al sistema, es str y NATES de procesarla debemos convertirla.



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






#* ⚠️Operador de la división entera "//", depende del tipo de dato del dividendo.




# ************************* 🔎OPERACION ARITMÉTICA: EL MODULO
# Devuelve el residuo de la división entre dos números. 
# Se expresa como: 10 modulo 4 → 



# ************************* OPERACIONES "ARITMÉTICAS" CON STRINGS
#? concatenacion: entre str con operador '+' 

#? multiplicacion de los strings: str '*' int


#! El resto de operaciones aritmeticas entre str y int/float no son posibles

#💡Haz casting para realizar operaciones, sean aritmeticas o concatenacion



#?*************************Notación Científica “E”
# Expresion resumida de una cifra numérica, con su exponente en base 10. 
# E || e El valor se guardará como TDD float.
# ®️ 2.5e3 = “2.5 multiplicado por 10 a la 3” =  2.5 × 10^3 = 2.5 * 1000 = 2500.0 

#? ➕E Positiva: El punto se mueve los dígitos E a la derecha y agregas 0 si es necesario.



#? ➖E Negativa: El punto se mueve los dígitos E a la izquierda y agregas 0 si es necesario.



#* Propiedades de las Potencias
# base con exponente positivo, se multiplica por sí mismo tantas veces como indique el exponente.


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