import streamlit as st
import pandas as pd
import plotly.express as px

# 1) Carga de datos
df = pd.read_csv("vehicles_us.csv")

# 2) Título y sección interactiva
st.title("Análisis Exploratorio de Coches")
st.header("Exploración interactiva de datos")

# 3) Botón para construir histograma
hist_button = st.button("Construir histograma")
if hist_button:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig = px.histogram(df, x="odometer", labels={"odometer": "Kilometraje (km)"})
    st.plotly_chart(fig, use_container_width=True)

# 4) Botón para construir gráfico de dispersión
scatter_button = st.button("Construir gráfico de dispersión")
if scatter_button:
    st.write("Creación de un gráfico de dispersión odómetro vs precio")
    fig_scatter = px.scatter(
        df,
        x="odometer",
        y="price",
        labels={"odometer": "Kilometraje (km)", "price": "Precio (USD)"},
        hover_data=["model_year", "model"],
        title="Odómetro vs Precio"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# 5) Visualizaciones fijas para referencia
st.subheader("Primeras filas de vehicles_us.csv")
st.dataframe(df.head())

st.subheader("Histograma de Kilometraje (fijo)")
fig2 = px.histogram(df, x="odometer", nbins=20, labels={"odometer": "Kilometraje (km)"})
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Relación Kilometraje vs Precio (fijo)")
fig3 = px.scatter(
    df,
    x="odometer",
    y="price",
    labels={"odometer": "Kilometraje (km)", "price": "Precio (USD)"},
    hover_data=["model_year", "model"]
)
st.plotly_chart(fig3, use_container_width=True)

# 6) Casilla de verificación para estadísticas básicas
if st.checkbox("Mostrar estadísticas básicas"):
    st.write(df.describe())
