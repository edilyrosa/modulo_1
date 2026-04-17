
#* Evita q el programa se interrumpa por error 

def dividir(a, b): return a/b

print(dividir(1, 3))
# print(dividir(1, 0)) #! ZeroDivisionError: division by zero
print('Soy el resto de la programacion ')
print(dividir(1, 2))


# def dividir_saneado(): 
#     inp1 = float(input('dividendo: '))
#     inp2 = float(input('divisor: '))
#     try:
#         return inp1/inp2
#     except ZeroDivisionError as e:
#         print(f'El error es: {e}')
#     except TypeError as e:
#         print(f'El error es: {e}')
#     except Exception as e:
#         print(f'El error es: {e}')
        
# print(dividir_saneado())

# print(dividir_saneado(1, 0))
# print(dividir_saneado(1, 'Ho')) #!TypeError: unsupported operand type(s) for /: 'int' and 'str'
# print(dividir_saneado(1, True))
# print('Soy el resto de la programacion')


#TODO: Existen las instrucciones: else y finally usadas en el bloque del manejo de las excepciones. INVESTIGALAS



def dividir_saneado():
    try:
        inp2 = int(input('Digite un denominador: '))
        inp1 = int(input('Digite un numerador: '))
        return inp1/inp2
    except ZeroDivisionError as e:
        print(f'1 ADRIAN El error es: {e}')
    except TypeError as e:
        print(f'2 ADRIAN  El error es: {e}')
    except ValueError as e:
        print(f'3 ADRIAN  El error es: {e}')
    except Exception as e:
        print(f'4 ADRIAN El error es: {e}')


print(dividir_saneado())    

# print(int('hola')) #ValueError: invalid literal for int() with base 10: 'hola'

# TODO: entonces cuales acciones u operaciones generan excepiones?
# casting de argumentos invalidos 
# div por 0
# intnetrar abrir files que no existen 
# interrumpir la ejecusion de con ctrl + c
# operaciones aritmeticas con tdd no nometicos