
#?⭐ ya sabemos recorrer, filtrar y mapear los iterables con los ciclos.

#? ⭐ Operador "in" 
#& 💡Recorrer iterables con Operador "in" 
print('💡Recorriendo una lista con Operador "in" ')
mi_lista = [10, 20, 30, 40, 50]
for e in mi_lista:
    if e > 30:
        print(e)

#& 💡Tambien podemos saber si un elemento existe en el iterable con Operador "in"

que_es = 5 in mi_lista
respuesta = '5 esta' if 5 in mi_lista else '5 no esta'
print(f'💡{respuesta}')



#? ⭐ Slicing de los iterables: para extraer (retornando) todo o parte de sus elementos.
# mi_lista[inicio: fin: paso] 
# 1. inicio: índice desde donde comienza el corte.
# Incluye el elemento en esta posición, Si se omite es indice 0.
# Puede ser negativo, contando desde el final.

# 2. fin: índice donde termina el corte. 
# Excluye el elemento en esta posición, Si se omite va hasta el final.
# Puede ser negativo para contar desde el final.

# 3. paso: Indica de cuánto en cuánto se avanza para tomar elementos.
# Por defecto es 1 → Toman elementos consecutivos de inicio a fin, -1 los toma a la inversa.
# No puede ser 0 (causa Error). 

lista_slicing = [1,2,3,4,5]
print('💡Haciendo Slicing de iterables')
print('todo', lista_slicing[::])
print('revs', lista_slicing[::-1])
print('revs', lista_slicing[::-2])


print('revs', lista_slicing[2::]) #[3,4,5]
print('revs', lista_slicing[:2:-1]) # #[4,5]


#?⭐⭐⭐ Lista compacta: 
# Forma resumida de crear una lista, es muy utilizadas profesionalmente, acostumbrate a esta sintaxis

#& 🤸🏻ESTO LO CONOCES con un ciclo for y una condición if.
mi_lista = [10, 21, 11, 51, 50]
mi_lista_filtrada = []

for e in mi_lista:
    if e %2 == 0:
        mi_lista_filtrada.append(e)
print(mi_lista_filtrada)

#& 💡HACIENDOLO COMPACTO CON LIST COMPREHENSION.
mi_lista_filtrada_comp = [e for e in mi_lista if e %2 == 0]
mi_tupla_filtrada_comp_generador = set(e for e in mi_lista if e %2 == 0)
print(mi_lista_filtrada_comp)
print(mi_tupla_filtrada_comp_generador)

#? al usar else, la sintaxis cambia !! 
#! mi_lista_filtrada_comp = [e for e in mi_lista if e %2 == 0 else 'impar']
mi_lista_filtrada_com_con_else = [e if e %2 != 0 else 'impar' for e in mi_lista] #✅

print(mi_lista_filtrada_com_con_else) # [10, 'impar', 'impar;, 'impar', 50]

# Crear una lista con elementos que NO son múltiplos de 2 de otra lista dada.

#? 🤸🏻EJERCICIO: Vamos a crear una lista compacta con elementos que NO son múltiplos de 2, o los impares
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_impares_sib = [ele for ele in lista_original if ele %2!=0]
lista_impares_neg = [x for x in lista_original if not x%2 == 0 ]
print('simb', lista_impares_sib)
print('negacion', lista_impares_neg)

#? ⭐ funcion range(start, stop, step)
# range(inicio, fin, paso), NO lo signo, lo recorro con un ciclo o lo convierto a lista, tupla, etc.
mi_range = range(5) 
print(mi_range)
print(list(mi_range))   #? cuando o uso para llenar una stuctura iterable, con su constructos
for e in mi_range:      #?cuando lo itero
    print(e)
print('otro rango')
for e in range(5,10):      #cuando lo itero
    print(e)


#? 🤸🏻 EJERCICO: realiza una lista compacta con 24 elementos: ["ciudad-1", "ciudad-2", ... "ciudad-24"]
num_ciudades = 25
range(1, 25)
ciudades = [f"ciudad-{num}" for num in range(1, num_ciudades)]
print(ciudades)  
    
#? ⭐ Desempaquetamiento de los iterables
# para extraer facilmente los elementos de iterables en variables, 
uno, dossss, tres, *rest = ciudades
print(uno)
print(dossss)
print(tres)
print(rest)

lista_mix = [rest, 'Edily', *range(1,5)]
print(lista_mix)

print('💡Impresion elementos unpacking de tupla con operador "*"')
#? 💡unpacking (operadores con el operador "*")


