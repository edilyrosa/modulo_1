
#* HEMOS VISTO LOS SIGUIENTES OPERADORES
# +, -, *, **, /, //, %                 → Aritmeticos.
#  += ,-+, *=, **=, /=, //=, %=         → Asignacion con
# ==, !=, >=, <= <, >,                  → Comparacion
 #& and, or not (En js son: &, ||, !)   → Logicos



# ***************Los operadores lógicos en Python CON PALABRAS (and, or, not), NO SIMBOLOS
# se utilizan para combinar expresiones booleanas (que son True o False). 
# Para tomar una decision o camino, basadas en varias condiciones al mismo tiempo.

# ***************Operador and (Y lógico):
# Devuelve True sólo si "ambas" condiciones son verdaderas.
# Si alguna es False, el resultado es False.

# ***************Operador or (O lógico):
# Devuelve True si "al menos una" condición es verdadera.
# Sólo devuelve False si todas las condiciones son falsas.

# ***************Operador not (Negación lógica):
# Invierte el valor booleano de una condición.
# Si la condición es True, not la convierte en False, y viceversa.
edad_usuario = 19
MAYORIDAD  = 18
# edad_usuario>= MAYORIDAD
print('Operadores Logicos')
print('True and True es: ', True and True) #T
print('True and False es: ', True and False) #F
print('False and False es: ', False and False) #F


print('True or True es: ', True or True) #T
print('True or False es: ', True or False) #T
print('False or False es: ', False or False) #F

solvente = True
print(not solvente) # False

#* Ejemplos prácticos

print('*********************🤸🏻🤸🏻‍♀️EJERCICIOS**************************')
# un "¡Día perfecto para un picnic!" serie igual a temperatura > 20 y hace_sol = True. 
# De lo contrario: "Mejor quedarnos en casa."
temperatura = 20
hace_sol = True
if temperatura >= 20 and hace_sol:
    print("1. ¡Día perfecto para un picnic! 🌞☀️" )
else:
    print("1. Mejor quedarnos en casa. 🏠" )
    
#? 🤸🏻Ejercicio: tienes_paraguas o hace_sol entonces print("¡Día perfecto para un picnic! 🌞☀️" )
# tienes_paraguas = True
# hace_sol = False

hace_sol = False
tienes_paraguas = True
if tienes_paraguas or hace_sol :
    print("2. ¡Día perfecto para un picnic! 🌞☀️" )
else:
    print("2. Mejor quedarnos en casa. 🏠" )


#& ⛹🏽⛹🏽 EJERCICIO 1: 
# como puedo expresar que: si es NO hace_sol: "Quizás deberíamos quedarnos en 🏠."
#& utilizando el operador not

hace_sol = False
if not hace_sol:
    print("Quizás deberíamos quedarnos en 🏠" )
else:
    print("Podemos salir porq hay sol" )

print(not hace_sol) #True
# TODO: 5_precedencia.py 

