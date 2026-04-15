
#* FUNCIONES EN PY.
# Las funciones son bloques de código reutilizables que realizan una tarea específica.
# Se definen usando la palabra clave def, seguida del nombre de la función y paréntesis ().
# Pueden aceptar parámetros (entradas) y devolver valores (salidas) usando la palabra clave return.


#?⭐ Definición de una función simple
def saludar(nombre):
    return f'Hola, {nombre}'      

#?⭐ Llamada a la función
print(saludar('Adrian'))
print(saludar('Edily'))
print(saludar('Eliana'))
print(saludar('Ana'))
#print(saludar()) #!TypeError: saludar() missing 1 required positional argument: 'nombre'


#?⭐ Función con múltiples parámetros
def sumar(a, b):
    return a + b

print(sumar(2, 5))
#print(sumar(2)) #!TypeError: sumar() missing 1 required positional argument: 'b'

#?⭐ Función sin parámetros
def obtener_pi():
    return 3.14159

print(3 + obtener_pi()) #6.14159


#?⭐ Función sin valor de retorno
def saludar_2(nombre): 
    print(f'Hola desde func 2, {nombre}')  

saludar_2('Carmen')


#?⭐ Función con valor por defecto en parámetros    
def potencia(base, exponente=2):
    resultado = base ** exponente
    print(resultado)
    return resultado

print(potencia(3))
print(potencia(3, 3))

