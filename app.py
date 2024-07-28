import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Analisis de autos usados')
car_data = pd.read_csv('vehicles_us.csv')

his_button = st.button('Construir histograma')

if his_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de disperción.')

if scatter_button:
    st.write('Creación de gráfico de disperción para el conjunto de datos de anuncios de coches.')

    fig = px.scatter(car_data, x='odometer', y='price')

    st.plotly_chart(fig, use_container_width=True)

build_boxplot = st.checkbox('Construir un bosplot')
if build_boxplot:    
    st.write('Construir un boxplot para la columna odometro')
    fig=px.box(car_data, x='condition', y='price', color='fuel')

    st.plotly_chart(fig, use_container_width=True)