# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:26:45 2021

@author: Gabriel E. Cabrera
"""

#%%""" Variables """

# = operador de asignación (no es el único)
ncel = 12345678 # el simbolo = es el de asignación
ncel

a = 1; b = 2; c = 3

a, b, c = 1, 2, 3

#%%""" Convenciones """

# librería
import keyword

# nombres reservados
keyword.kwlist

# esto es un comentario simple

"""
esto 
es 
un 
comentario
multiple
"""

#%%""" Tipos de Datos (escalares) """

'''Tipos básicos de datos'''
# integers
integer = 2 
type(integer) # identificación
isinstance(integer, int)  # identificación 

# float
floating = 3.14
type(floating)
isinstance(floating, float)

# string
string = "hola mundo"
type(string)
isinstance(string, str)

# boolean
boolean = True
type(boolean)
isinstance(boolean, bool)

'''casting'''
# integers
int('1')
int(True)
int(False)

# float
float('1')
float(True)
float(False)

# string
str(1)
str(True)
str(False)

# boolean
bool(1)
bool(0)

#%%
"""
Expresiones numéricas
"""

'''1'''
a = 4
b = 3

# suma
a + b

# resta
a - b

# multiplicación
a * b

# división
a / b

# modulo
a % b

# parte entera
a // b

# potencia
a ** b

'''2'''
1 + 2 ** 3 / 4 * 5

'''3'''
valor_presente = 1000 / (1 + 0.1) ** 1 +  1000 / (1 + 0.1) ** 2 + 1000 / (1 + 0.1) ** 3 + 1000 / (1 + 0.1) ** 4 + 1000 / (1 + 0.1) ** 5
print('El valor presente es: ' + str(valor_presente))

#%%
"""
Cadenas de texto
"""

'''1.a'''
texto = 'Hay ciertas cosas que el dinero no puede comprar, para todo lo demás existe mastercard'
len(texto)

# primer caracter
texto[0]

# primeros 5 caracteres
texto[0:5]

# último caracter
texto[-1]

'''1.b'''
texto.count('r')
texto.count('r', texto.find(','))

'''1.c'''
texto.find('mastercard')

'''1.d'''
texto.replace('mastercard', 'Mastercard')


'''2.a'''
lower_name = "guido von rossum"
lower_name.upper()

'''2.b'''
lower_name.title()


'''3'''
# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
template = '{0:.2f} {1:s} equivale a $CLP{2:d}'
template.format(2.45535, 'dolares', 1808)


'''4'''
# concatenación, deben ser str()
'2' + '25'

#%%
"""
Lógica Booleana
"""

'''1'''
a = 4
b = 3

'''operadores de comparación'''
# mayor que 
a > b

# menor que
a < b

# igual a
a == b

# distinto a
a != b

# mayor o igual a
a >= b

# menor o igual a
a <= b

''' operadores lógicos'''
x = True
y = False

# True y False = False
x and y

# True o False = True
x or y 

# no True = False
not x


'''2'''
texto = 'Hay ciertas cosas que el dinero no puede comprar, para todo lo demás existe mastercard'

# operador afiliación (membership)
'''2.a'''
'z' in texto

'''2.b'''
'm' in texto

'''2.c'''
'visa' in texto


'''3'''
A = True
B = False

not(A and B) == (not(A) or not(B))

A = False
B = True

not(A and B) == (not(A) or not(B))

A = True
B = True

not(A and B) == (not(A) or not(B))

A = False
B = False

not(A and B) == (not(A) or not(B))