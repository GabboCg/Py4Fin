# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:02:01 2021

@author: Habac
"""

#%%''' Aplicaciones '''

'''1.a'''
# importa pandas 
import pandas as pd 

# "lee" xlsx
gapminder = pd.read_excel('gapminder.xlsx')

# "lee" dta formato de stata
pd.read_stata('gapminder.dta')

#%% 
'''2.a'''
# 10 primeras observaciones
gapminder.head()

# 10 últimas observaciones
gapminder.tail()

#%%
'''3.a'''
# extrae columnas
gapminder.columns

# extrae rl column index de la columna continent
gapminder.columns.get_loc('continent')

# extrae index
gapminder.index

# valores únicos de la variable continent
gapminder.continent.unique()

'''
Seleccionar variables (columnas) de un DataFrame
'''
# forma 1: 
# selecciona la variable continent como series
gapminder.continent

# forma 2: 
# selecciona la variable continent como series
gapminder['continent']

# forma 3: 
# selecciona la variable continent como series utilizando loc (se puede seleccionar filas)
gapminder.loc[:,'continent']
# selecciona la variable continent como series utilizando iloc (se puede seleccionar filas)
gapminder.iloc[:,1]

# forma 4: 
# selecciona la variable continent y lifeExp utilizando loc (se puede seleccionar filas)
gapminder.loc[:,['continent','lifeExp']]
# selecciona la variable continent y lifeExp utilizando iloc (se puede seleccionar filas)
gapminder.iloc[:,[1,3]]

# forma 5: 
# selecciona las variables desde continent hasta pop (la incluye) utilizando loc (se puede seleccionar filas)
gapminder.loc[:,'continent':'pop']
# selecciona las variables desde continent hasta pop (4) utilizando iloc (se puede seleccionar filas)
gapminder.iloc[:,1:5]

# forma 6: 
# selecciona la variable continent y lifeExp (no se puede seleccionar filas)
gapminder[['continent','lifeExp']]

'''
Seleccionar variables (columnas) de un DataFrame
'''
# filtra continent == "Americas"
gapminder[gapminder['continent'] == "Americas"]

# filtra continent == "Americas" o filtra continent == "Asia"
gapminder[(gapminder['continent'] == "Americas") | (gapminder['continent'] == "Asia")]

# filtra (continent == "Americas" o filtra continent == "Asia") y year == 2007
gapminder[((gapminder['continent'] == "Americas") | (gapminder['continent'] == "Asia")) & (gapminder['year'] == 2007)]
          
# filtra continent == "Americas" o filtra year == 2007
gapminder1 = gapminder[(gapminder['continent'] == "Americas") & (gapminder['year'] == 2007)]

#%%
'''4.a'''
# ordena los valores de mayor a menor y muestra la primera observación
gapminder1.sort_values(['gdpPercap'], ascending=False).head(1)

# ordena los valores de menor a mayor y muestra la última observación
gapminder1.sort_values(['gdpPercap'], ascending=False).tail(1)

#%%
'''5.a'''
# reinicia el índice y lo "bota"
gapminder1 = gapminder1.reset_index(drop=True)

# elimina/remueve la variable (columna) continent y year (axis=1)
gapminder1 = gapminder1.drop(['continent','year'], axis = 1)

# elimina/remueve la fila con índice 0 y 1 (axis=0)
gapminder1.drop([0,1], axis=0)

# agrega como índice el país, lo realiza in-place
gapminder1.set_index('country', inplace=True)

# elimina/remueve la fila con el índice igual a Ecuador
gapminder1.drop(['Ecuador'], axis=0)

#%%
'''6.a'''
# re-asigna a la columna el nombre original pero en minuscula 
gapminder1.columns = [i.lower() for i in list(gapminder1.columns)]

# renombra la columna country por pais
gapminder.rename(columns={'country':'país'})

#%%
'''7.a'''
# genera la variable lifeeexp * 12 y la asigna al DataFrame gapminder1
gapminder1['lifeexp_mes1'] = gapminder1['lifeexp'] * 12

# genera la variable lifeeexp * 12 y la asigna al DataFrame gapminder1 utilizando una función anónima
gapminder1['lifeexp_mes2'] = gapminder1['lifeexp'].apply(lambda x: x * 12) 

# genera la variable lifeeexp * 12 y la asigna al DataFrame gapminder1 definiendo primero una función 
def mensual(x):
    res = x * 12
    return(res)

# si no se selecciona una columna lo aplica a todo el DataFrame
gapminder1['lifeexp_mes3'] = gapminder1['lifeexp'].apply(mensual) 

#%%
'''8.a'''
df_europe = gapminder[(gapminder['continent'] == "Europe")].copy()
df_europe.reset_index(drop=True, inplace=True)

'''8.b'''
# agrupa por country y aplica el crecimiento en una función anónima
df_europe['gdpgrowth'] = df_europe.groupby('country')['gdpPercap'].apply(lambda x: (x / x.shift(1) - 1))

'''8.c'''
df_europe.dropna(subset=['gdpgrowth'], inplace=True) # selecciona un subconjunto (gdpgrowth) y los elimina in-place
df_europe.dropna() # elimina todos los NA (fila y columna)

'''8.d'''
# promedio por país agrupado
df_europe.groupby('country').mean()
# describe por país agrupado
desc_stat = df_europe.groupby(['country']).describe()

'''8.e'''
# exporta a excel la estadística descriptiva
desc_stat.to_excel("desc_stat_europe.xlsx")