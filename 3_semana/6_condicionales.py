
#& 1. IF
#Se ejecuta un bloque si la condición es verdadera.
# Sintaxis: 
# if condición lógica a evaluar :
#   indentación →  código py a ejecutar

#? Sentencia else
#Se usa para definir qué sucede si la condición del if es falsa. 
# Por eso NO LE SIGUE NINGUNA condición lógica a evaluar.  
# Se Ejecuta si ninguna condición previa es verdadera.

#?⭐ Ejercicio: Determine si un número es par o impar, 💡solo existen esas 2 posibilidades, si el dato es numerico.
# print('Veamos si el nuemro es par')
# num = int(input('Digite el numero a evaluar: '))
# if num % 2 == 0:
#     print(f'El numero {num} es par')
# else: 
#     print(f'El numero {num} es INpar')

    
#& 2. ELIF
# Es la forma de agregar múltiples condiciones a una sentencia if-else. 
#? Ejercicio: catalogue a un estudiante según su calificación, 
# con rangos de {
# +90,  -> # Excelente 🥳
# +80,  -> # Muy bien 👏
# +70,  -> # Bien 👍
# +60,  -> # Suficiente 👌
# else -> # Insuficiente 😞
# }
# print('Calificando notas')
# nota = int(input('Digite la nota del alumno: '))
# if nota < 1  or  nota >100:
#     print('Nota FUERA DE RANGO')
# elif nota >= 90:
#     print('Nota Excelente 🥳')
# elif nota >= 80:
#     print('Nota Muy bien 👏')
# elif nota >= 70:
#     print('Nota Bien 👍')
# elif nota >= 60:
#     print('Nota Suficiente 👌')
# else:
#     print('Nota Insuficiente 😞')
    

#& IF - ANIDADOS
# # Determine si usuario puede Conducir?
# # condicion: debe tener licencia (True/False) AND ( (ser mayor de edad (>=18)  OR estar emancipado (si/no) )


# #? TERNARIO
# Es una forma corta de escribir una sentencia if-else en una sola línea.
# Sintaxis: valor_si_verdadero if condición else valor_si_falso

# f = bool(0) #F
# t = bool(12)
# print(f, t)

print('\n 🤸🏻 Ejercicio: Asignamos a una variable bandera de usuario autenticado o no')
autenticado = bool(int(input('Usuario esta autenticado: (0/1): ')))
print(type(autenticado), autenticado)
mensaje = '✅Esta autenticado' if autenticado == True else '❌ NO Esta autenticado' 
print(mensaje)


# TODO PROXIMO_TEMA:
#  EJERCICIO WEB LOGIN CONDICIONALES Y OPERADORES COMPARACION




