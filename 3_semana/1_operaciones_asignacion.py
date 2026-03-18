
# ******************Operadores de asignación compuestos
# Permiten realizar una operación con el valor actual de la variable y luego 
# asignar el resultado a esa misma variable. Son equivalentes a escribir la operación completa 
# con asignación, pero en forma abreviada.

#* ®️Resumen
# ✅El operador = asigna un valor directamente.
# ✅💡Los operadores compuestos (+=, -=, *=, etc.) 
# modifican la variable basándose en su valor actual.
# ✅Son útiles para escribir código más limpio y eficiente.


# + - * ** / // %
#*  += -+ *= **= /= //= %=
x = 5
x +=5 #10
x -=2 #8
x *=10 #80
x /=2 #40.0
x //=4 #10.0
x %=4 #2.0
x **=0 #1.0

print(x) 



print('Ejercicios')
a = 7
b = 2

x = a # 7
x += b  #9             
print('x += b:', x)   


# #TODO: 3_op_comparacion.py