# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:22:43 2020

@author: Pablo Sao
"""
import plotly.express as px
import pandas as pd


def DisplayScatterPlot(Data,X,Y,hoverData,Titulo,t_ejex,t_ejey):
    
    fig = px.scatter(Data, x=X, y=Y,color="release_year",
                     size='runtime', hover_data=hoverData)
    
    fig.update_layout(title=Titulo)
    fig.update_yaxes(title_text=t_ejex)
    fig.update_xaxes(title_text=t_ejey)
                     
    fig.show()
    

def DisplayLinePlot(Data,X,Y,hoverData,Titulo,t_ejex,t_ejey):
    
    serie_tiempo = px.line(Data, x=X, y=Y,color="release_year",
                       hover_data=hoverData)
    serie_tiempo.update_layout(title=Titulo)
    serie_tiempo.update_yaxes(title_text=t_ejey)
    serie_tiempo.update_xaxes(title_text=t_ejex)
    
    serie_tiempo.show()



# Cargando data
data = pd.read_csv('tmdb-movies.csv')


columns = ['imdb_id', 'popularity','cast','homepage','keywords','overview',
           'production_companies','tagline','budget_adj','revenue_adj','genres']
data.drop(columns, inplace=True, axis=1)

data.dropna()

data['release_date'] =  pd.to_datetime(data['release_date'], infer_datetime_format=True)


print(data.dtypes)

#data = data.dropna()

# data['release_date'] =pd.to_datetime(data['release_date'])

#data.sort_values(by='release_date', inplace=True, ascending=False)


data["runtime"]=data["runtime"].div(60).round(2)

#calculando la ganancia
data["monto_ganancia"] = data["revenue"] - data["budget"]

#print(data.head())

# Graficando Ganancia vs Presupuesto
titulo = 'Ganancias vs Inversion'
titulo_ex = "Inversión"
titulo_ey = "Ganancia"
HoverData = ['original_title']

DisplayScatterPlot(data,data["budget"],data["revenue"],HoverData,
                   titulo,titulo_ex,titulo_ey)

# Graficando serie de tiempo de ganancia vs fecha estreno

titulo = 'Ganancia vs Fecha Estreno'
titulo_ex = "Fecha Estreno"
titulo_ey = "Ganancia (Ingresos - Presupuesto)"
HoverData = ['original_title','monto_ganancia']

DisplayLinePlot(data,data["release_date"],data["monto_ganancia"],
                HoverData,titulo,titulo_ex,titulo_ey)




