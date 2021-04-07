# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:25:58 2021

@author: Habac
"""

# lista como "matriz"
x = list([[1,2,3],[4,5,6],[7,8,9]])
x

# extracción elemento ij
x[1][1]

# carga librería numpy
import numpy as np

mat_x = np.array(x) # se genera el array
mat_x

mat_x.ndim # posee dos dimensiones

m, n = mat_x.shape # número de filas y columnas
m, n

mat_x.size # número de elementos en la matriz

# se verifica la class array
type(mat_x)

# la versión de range pero en numpy
np.arange(1,10).reshape(-1,3)

#%% '''NumPy'''

'''1.a'''
num = [3, 0, 2, 2, 0, 2, 0, 1, 1]

list_to_array = np.array(num)
a = list_to_array.reshape((3,3))

# forma 1
a.T

# forma 
a.transpose()

'''1.b'''
b = np.linalg.inv(a)

'''1.c'''
a.dot(b)

# para generar una matriz identidad 
np.eye(3)

'''1.d'''
mean_a = np.ones((1,3)).dot(a).dot(np.ones((3,1))) / a.size
mean_a[0][0]


'''2.a'''
c = np.array([[2,4],[5, -6]])
d = np.array([[9,-3],[3,6]])

# suma 
c + d
# resta
c - d
# multiplicación
c * d
# división
c / d

'''2.b'''
c.dot(d)


'''3.a'''
mat_a = np.array([[1,2,3],[4,5,6]])
mat_b = np.array([[1,2,3],[4,5,6]])

def manual_mult(mat_a, mat_b):
  '''
  multiplica el elemento ij de la matriz a con el elemento ij de la matriz b 
  ''' 
  m,n = mat_a.shape

  zero_mat = np.zeros((m,n))
  zero_mat.fill(np.nan)

  for i in range(m):
    for j in range(n):
      zero_mat[i][j] = mat_a[i][j] * mat_b[i][j] 

  return(zero_mat)

# probamos la función
manual_mult(mat_a, mat_b)

#%% '''Números Aleatorios'''

'''1.a'''
np.random.seed(10)

array_norm = np.random.randn(10000)

# reshape
e = array_norm.reshape((100,100)) 

# resize
array_norm.resize((100,10), refcheck=False)
array_norm # in-place, pero no debe haber sido referenciado por ejemplo con reshape

'''2.b'''
e_flatten_col = e.flatten(order='C') # aplanado por columna
e_flatten_row = e.flatten(order='F') # aplanado por fila

e_flatten_col.mean() # promedio
e_flatten_col.std() # desviación estandar

array_norm

#%% '''sistema de Ecuaciones'''

'''1.a'''
# se genera las matrices (incógnita + resultado)
mat1 = np.array([[1, 1, 1], [3, -2, 1], [2, 1, -1]])
mat1_res = np.array([6, 2, 1])

# se resuelve el sistema de ecuaciones
np.linalg.solve(mat1, mat1_res)

'''1.b'''
# se genera las matrices (incógnita + resultado)
mat2 = np.array([[3, 4, -5, 1], [2, 2, 2, -1], [1, -1, 5, -5], [5, 0, 0, 1]])
mat2_res = np.array([10, 5, 7, 4])

# se resuelve el sistema de ecuaciones
np.linalg.solve(mat2, mat2_res)