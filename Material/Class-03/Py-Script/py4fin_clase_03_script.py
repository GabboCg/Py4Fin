# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:52:26 2021

@author: Gabriel E. Cabrera
"""

#%%''' Loop (ciclo) con & sin range() '''

'''1.a'''
lista1 = ['Facebook', 'Apple', 'Amazon', 'Netflix']

for tech in lista1:
  print('Empresa:'+tech)

'''1.b'''
for i, tech in enumerate(lista1):
  print('índice:'+str(i)+','+'Empresa:'+tech)

'''1.c'''
for tech in lista1:
  for i, letra in enumerate(tech):
    print('n°:'+str(i)+','+'Letra:'+letra+','+'Empresa:'+tech)


'''2.a'''
for num in range(0,11):
  print(num)


'''3.a'''

for num in reversed(range(0,11)):
  print(num)

#%%''' Condicionales '''

'''1.a'''
seq = [1, 2, None, 4, 5, 6, None]

# variable igual a cero
total = 0

for j in seq:
  if j == None:
    continue    
  else:
    total += j

print('La suma total es: '+str(total))


'''2.a'''
seq1 = [1, 2, None, 4, 5, 6, None]

# variable igual a cero
total1 = 0

for j in seq1:
  if j == None:
    break   
  else:
    total1 += j

print('La suma total es: '+str(total1))


'''3.a'''
seq2 = list(range(1,8))

# forma 1
total2 = 0

for j in seq2:
  if j < 5:
    total2 += j
  elif j == 5:
    print(str(j)+' es igual a 5')
  else:
    print(str(j)+' es mayor a 5')
  
total2


'''4.a'''
seq2 = range(16)

total3 = 0

for k in seq2:
  if (k%3 == 0) or (k%5 == 0):
    total3 += k
  else:
    print(str(k)+' no es múltiplo de 3 o 5')

total3


'''5.a'''
fib = []

fib.append(0)
fib.append(1)

x = 1

while x <= 12:
  res = fib[x] + fib[x - 1] 
  fib.append(res)
  x += 1

fib

#%%''' Comprehension '''

'''1.a'''
# lista 
list2 = ['Facebook', 'Apple', 'Amazon', 'Netflix']

# iteración con comprehension
list2_title = [elem.upper() for elem in list2]
list2_title

# iteración estandar
list2_title2 = []

for elem in list2:
  list2_title2.append(elem.upper())

list2_title2


'''2.a'''
# con ifelse statement
[num if (num%3 == 0) or (num%5 == 0) else None for num in range(16)]

# iteración estandar
res2 = []

for num in range(16):
  if (num%3 == 0) or (num%5 == 0):
    res2.append(num)
  else:
    res2.append(None)

res2


'''3.a'''
# lista anidada
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[sub_elem for elem in nested_list for sub_elem in elem]

flattened_list = []

for elem in nested_list:
  for sub_elem in elem:
    flattened_list.append(sub_elem)

flattened_list
