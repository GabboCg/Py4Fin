# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:52:26 2021

@author: Gabriel E. Cabrera
"""

#%%''' Lista (list) '''

'''1.a'''
faan = ['Facebook', 'Apple', 'Amazon', 'Netflix']

# n° de elementos en la lista
len(faan)

# solo el primer elemento 
faan[0]

# solo el segundo elemento 
faan[1]

# solo el tercer elemento 
faan[2]

# solo el último elemento
faan[3]

# todos los elementos
faan[:]

# primer elemento más todos los demás
faan[0:]

# segundo elemento más todos los demás
faan[1:]

# primer elemento hasta el tercer elemento (inclusive), el intervalo será [,)
faan[0:3]

# seleccionar todo usando un índice inexistente en la lista pero mayor al existente
faan[0:1000]

'''1.b'''
# primer elemento
faan[-4]

# último elemento
faan[-1]

'''1.c'''
faan.insert(0, 'Nvidia') # in-place 
faan.insert(3, 'Nvidia') # cuarta posición (in-place)

'''1.d'''
faan.append('Google') # importante (in-place) por default es la última posición

'''1.e'''
len(faan)

'''1.f'''
faan.index('Apple') # mostrará la primera posición que contenga el elemento, pero no todos los que existan en la lista

'''1.g'''
# forma 1
del faan[faan.index('Nvidia')] # mostrará el primero 
del faan[faan.index('Netflix')]

# forma 2 
faan.pop(faan.index('Nvidia')) # .pop() por default remueve el último
faan.pop(faan.index('Netflix'))

# forma 3
faan.remove('Nvidia')
faan.remove('Netflix')

'''1.h'''
faan.sort(key=len)

#%%''' Tupla (tuple) '''

'''2.a'''
parte_a = [[0, 'a'], [1, 'b']]
parte_b = [[2, 'c'], [3, 'd']]

lista_combinada1 = parte_a + parte_b

# usando extend
parte_a.extend(parte_b) # in-place

'''2.b'''
# elementos en la lista anidada
lista_combinada1[0]
lista_combinada1[0][0]
lista_combinada1[0][1]


'''3.a'''
num_list = list(range(1, 11))

# sort
num_list.sort(reverse=True) # in-place

# sorted (bult-in)
sorted(num_list) 

'''3.b'''
num_list[::2]

tupla = 1, 2, 'Facebook', 'Amazon'
tupla

tupla_anidada1 = (1,2), ('Facebook', 'Amazon')
tupla_anidada1

tupla_anidada2 = (1,2), ('Facebook', 'Amazon'), ['Apple', 'Netflix']
tupla_anidada2

tupla_anidada2[2].append('Google')
tupla_anidada2

('Facebook', 'Amazon') + ('Apple', 'Netflix')

('Facebook', 'Amazon') * 3

tuple([1, 2, 3, 4])

#%%''' Diccionario (dict) '''

dict1 = {'Name' : 'Janet Yellen', 
         'Country' : 'United States',
         'Profession' : ' United States secretary of the treasury',
         'Age' : 74}
        
type(dict1)

print(dict1['Name'], dict1['Age'])

dict1.keys() # keys (llaves)

dict1.values() # valores

dict1.items()  # items = keys + values

#%%''' Conjunto (set) '''

set1 = set([1, 2, 3, 4, 5, 5])
set1

set2 = set([3, 4, 5, 6, 9, 9, 7])
set2

# union
set1.union(set2)

# intersección
set1.intersection(set2)

set1.difference(set2)

set2.difference(set1)

set1.symmetric_difference(set2)