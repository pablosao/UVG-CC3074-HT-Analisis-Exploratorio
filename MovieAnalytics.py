# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:22:43 2020

@author: Pablo Sao
"""
import plotly.express as px
import pandas as pd

# Cargando data
data = pd.read_csv('tmdb-movies.csv')

data["runtime"]=data["runtime"].div(60).round(2)

X = data["budget"]
Y = data["revenue"]

fig = px.scatter(data, x=X, y=Y,color="release_year",
                 size='runtime', hover_data=['original_title'])

fig.update_layout(title='Ganancias vs Inversion')
fig.update_yaxes(title_text="Ganancia")
fig.update_xaxes(title_text="Inversion")
                 
fig.show()


