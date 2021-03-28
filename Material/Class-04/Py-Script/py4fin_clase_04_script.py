# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:25:58 2021

@author: Habac
"""
#%%''' Aplicaciones '''

'''1.a'''
def elevado(n):
  total = 0
  for i in range(1,n+1):
    total += i ** 2
  return(total)

elevado(5)

'''1.b'''
def divisible(n):
  if (n % 4) == 0:
    return(print('El número '+str(n)+' es divisible por 4.'))
  else:
    return(print('El número '+str(n)+' no es divisible por 4.'))

divisible(16)

'''1.c'''
def media_aritmetica(n):
  output = sum(n) / len(n)
  return(output)

media_aritmetica([1,2,3,4,5])

'''1.d'''
def valor_neto_presente(flujo, tasa):
   total = 0
   for i, num in enumerate(flujo):
     if i == 0:
       total += num
     else:
       total += num / (1 + tasa) ** (i) 
   return(total)

flujos = [-500000,100000,150000,180000,200000,300000]

valor_neto_presente(flujos, 0.12)

#%%''' Funciones Anónimas (Lambda) '''

seq = [1, 2, 4]

def apply_a_una_lista(lista, f):
    return [f(x) for x in lista]

apply_a_una_lista(seq, lambda x: x ** 2)

#%%''' Importar Funciones''' 

# tiene que estár en el mismo directorio, si se * y no el nombre de cada función se cargan todas las funciones disponibles
from funciones_auxiliares import media_aritmetica, valor_neto_presente 

# función de 1.3
media_aritmetica([1,2,3,4,5])

# función de 1.4
flujos = [-500000,100000,150000,180000,200000,300000]

valor_neto_presente(flujos, 0.12)