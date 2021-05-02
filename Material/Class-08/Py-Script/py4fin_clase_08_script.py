# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:02:01 2021

@author: Habac
"""
#%% '''API Yahoo Finance'''
'''1.a'''
# importa pandas
import pandas as pd
# import numpy
import numpy as np 
# import ytfinance
import yfinance as yf 

# ticker 
asset = "GME"

# descarga la información OHCL del GameSpot
gme_ohcl_daily = yf.download(asset, start = "2015-01-01", end = "2021-03-01")

'''1.b'''
# breve estadística descriptiva
gme_ohcl_daily.apply(lambda x: x.describe())

'''1.c'''
# se extrae año
gme_ohcl_daily['Year'] = gme_ohcl_daily.index.year
# se extrae mes
gme_ohcl_daily['Month'] = gme_ohcl_daily.index.month
# se extrae día
gme_ohcl_daily['Day'] = gme_ohcl_daily.index.day

'''1.d'''
# se selecciona el adj close
gme_close_daily = gme_ohcl_daily.loc[:,['Close']]

#%%'''Cambios a través del tiempo'''
'''2.a'''
# se aplica el método diff()
gme_close_daily['diff'] = gme_close_daily[['Close']].apply(lambda x: x.diff())

'''2.b'''
# se aplica el método shift()
gme_close_daily['close_t_1'] = gme_close_daily[['Close']].apply(lambda x: x.shift(1))      

'''2.c'''
# se divide (1) por (2)
gme_close_daily['returns'] = gme_close_daily['diff'] / gme_close_daily['close_t_1']

'''2.d'''
# se utiliza el método pct_change()
gme_close_daily['pct_change'] = gme_close_daily[['Close']].apply(lambda x: x.pct_change(1))  

#%% '''Visualización Básica de Series de Tiempo'''
'''3.a'''
# importa matplotlib
import matplotlib.pyplot as plt

# gráfico de linea 
fig1 = gme_ohcl_daily.loc[:,'Close'].plot(kind='line', figsize=(13,5), lw=2) # se crea un gráfico de linea 
fig1.grid(color='grey', linestyle=':')                                       # cambia el estilo de la grilla
fig1.set_title('Precio al Cierre de GameSpot (GME)', fontsize=14, y=1.00)    # agrega título
fig1.set_xlabel('')                                                          # nombre del eje x
fig1.set_ylabel('Close')  

# guarda el gráfico con el nombre fig1.png
plt.savefig('fig1.png', dpi=300)

#%% '''Análisis Técnico: Media Movil'''
'''3.a'''
# selecciona precio cierre
tech_analysis = gme_ohcl_daily.loc[:,['Close']]

# mínimo movil a 20 días
tech_analysis['Min'] = gme_ohcl_daily['Close'].rolling(window=20).min()
# media movil a 20 días
tech_analysis['SMA1'] = gme_ohcl_daily['Close'].rolling(window=20).mean()
# máximo móvil a 20 días
tech_analysis['Max'] = gme_ohcl_daily['Close'].rolling(window=20).max()

# elimina NAs in-place
tech_analysis.dropna(inplace=True)

# dataframe filtrada
df2 =  tech_analysis.loc[:,['Min','Close','SMA1','Max']][(tech_analysis.index >= "2020-01-01") & (tech_analysis.index <= "2020-09-08")]

fig2 = df2.plot(figsize=(13,5), style=['g--', 'b-', 'r--', 'g--'], lw=2)   # se crea un gráfico de linea  
fig2.grid(color='grey', linestyle=':')                                     # cambia el estilo de la grilla
fig2.set_title('Rolling a 20 días de GameSpot (GME)', fontsize=14, y=1.00) # agrega título
fig2.set_xlabel('')                                                        # nombre del eje x
fig2.set_ylabel('Close')                                                   # nombre del eje y 

# guarda el gráfico con el nombre fig2.png
plt.savefig('fig2.png', dpi=300)

'''3.b'''
# media movil a 252 días
tech_analysis['SMA2'] = gme_ohcl_daily['Close'].rolling(window=252).mean()
# pisición usando np.where()
tech_analysis['Positions'] = np.where(tech_analysis['SMA1'] > tech_analysis['SMA2'], 1, -1)

# elimina NAs in-place
tech_analysis.dropna(inplace=True)

# selecciona SM1, Close, SMA2 y Positions
df3 = tech_analysis.loc[:,['SMA1','Close','SMA2','Positions']][(tech_analysis.index >= "2020-01-01") & (tech_analysis.index <= "2020-09-08")]

# fig (figura) y ax1 (axis)
fig, ax1 = plt.subplots(figsize=(13,5)) # # se crea un subplot

lns1 = ax1.plot(df3.loc[:,['SMA1']], color='green', label="SMA1", linestyle='--', lw=2) # se crea un gráfico de linea
lns2 = ax1.plot(df3.loc[:,['Close']], color='blue', label="Close", linestyle='-', lw=2) # se crea un gráfico de linea
lns3 = ax1.plot(df3.loc[:,['SMA2']], color='green', label="SMA2", linestyle='--', lw=2) # se crea un gráfico de linea

# nombre eje y
ax1.set_ylabel('Close')

# crea segundo eje que comparte el mismo eje de ax1
ax2 = ax1.twinx()  

# se crea un gráfico de linea para el eje secundario
lns4 = ax2.plot(df3.loc[:,['Positions']], color='red', label="Pos.", linestyle='--', lw=2)

# nombre eje y (secundario)
ax2.set_ylabel('Positions')

# se suman los gráfico de linea 
lns = lns1 + lns2 + lns3 + lns4
labs = [l.get_label() for l in lns] # extrae etiqueta

# configuración de la leyenda
ax1.legend(lns, labs, loc=2, facecolor="white", shadow=True)

# ajuste de la grilla
ax1.grid(color='grey', linestyle=':', axis='both')

# título
fig.suptitle('Indicador Técnico: Media Movil 20 y 252 días | GameSpot (GME)', fontsize=14, y=0.925)

# guarda el gráfico con el nombre fig3.png
plt.savefig('fig3.png', dpi=300)

'''3.c'''
# importa plotly
import plotly.graph_objects as go

# filtra los datos OHCL
df_plotly = gme_ohcl_daily[(gme_ohcl_daily.index >= "2020-01-01") & (gme_ohcl_daily.index <= "2020-09-08")]

# grafica candlestick
fig_plotly = go.Figure(data=[go.Candlestick(x=df_plotly.index,
                                            open=df_plotly['Open'],
                                            high=df_plotly['High'],
                                            low=df_plotly['Low'],
                                            close=df_plotly['Close'])])

# se visualiza
fig_plotly.show()

#%% '''Descargar Multiples índices'''
'''4.a'''
# tickers a descargar
tickers = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOG']

# se descarga y se guarda en un diccionario
FAANG = {i: yf.download(i, start = "2000-01-01", end = "2021-03-01", interval='1mo') for i in tickers}
# cada precio al cierre lo pasa a una lista
FAANG_Close = [k[['Close']].dropna().rename(columns={'Close':j}) for j, k in FAANG.items()]

# concatena cada DataFrame por índice (basado en la columna)
df_concat = pd.concat(FAANG_Close, axis=1)

fig4 = df_concat.dropna().plot(figsize=(13,5), lw=2)                       # se crea un gráfico de linea 
fig4.grid(color='grey', linestyle=':')                                     # cambia el estilo de la grilla
fig4.set_title('Evolución Precios al Cierre | FAANG', fontsize=14, y=1.00) # agrega título
fig4.set_xlabel('')                                                        # nombre del eje x
fig4.set_ylabel('Close')                                                   # nombre del eje y 

# guarda el gráfico con el nombre fig4.png
plt.savefig('fig4.png', dpi=300)

'''4.b'''
# de columnas a filas
df_melted = df_concat.melt(var_name="Symbol", value_name="Close", ignore_index=False)

# se verifica el df
df_melted

'''4.c'''
# de filas a columnas
df_pivoted = df_melted.pivot(columns='Symbol', values='Close')

# se verifica el df
df_pivoted