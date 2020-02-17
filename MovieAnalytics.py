# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:22:43 2020

@author: Pablo Sao
"""
import plotly.express as px
import pandas as pd

# Cargando data
data = pd.read_csv('tmdb-movies.csv')

#data = data.dropna()

# data['release_date'] =pd.to_datetime(data['release_date'])

#data.sort_values(by='release_date', inplace=True, ascending=False)


data["runtime"]=data["runtime"].div(60).round(2)

#calculando la ganancia
data["monto_ganancia"] = data["revenue"] - data["budget"]

#print(data.head())

X = data["budget"]
Y = data["revenue"]

# Graficando Ganancia vs Presupuesto
fig = px.scatter(data, x=X, y=Y,color="release_year",
                 size='runtime', hover_data=['original_title'])

fig.update_layout(title='Ganancias vs Inversion')
fig.update_yaxes(title_text="Ganancia")
fig.update_xaxes(title_text="Inversion")
                 
fig.show()


# Graficando serie de tiempo de ganancia vs fecha estreno

#Calculando presupuesto

X = data["release_date"]
Y = data["monto_ganancia"]

serie_tiempo = px.line(data, x=X, y=Y,color="release_year",
                       hover_data=['original_title','monto_ganancia'])

serie_tiempo.update_layout(title='Ganancia vs Fecha Estreno')
serie_tiempo.update_yaxes(title_text="Ganancia (Ingresos - Presupuesto)")
serie_tiempo.update_xaxes(title_text="Fecha Estreno")

serie_tiempo.show()
