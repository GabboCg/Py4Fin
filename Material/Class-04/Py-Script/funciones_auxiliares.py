# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:25:58 2021

@author: Habac
"""

def media_aritmetica(n):
  output = sum(n) / len(n)
  return(output)

def valor_neto_presente(flujo, tasa):
   total = 0
   for i, num in enumerate(flujo):
     if i == 0:
       total += num
     else:
       total += num / (1 + tasa) ** (i) 
   return(total)