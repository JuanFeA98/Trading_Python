import streamlit as st
from datetime import date

from plotly import graph_objects as go

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

from Utils.functions import load_data, plot_raw_data

# Variables globales
START = '2020-01-01'
TODAY = date.today().strftime("%Y-%m-%d")

stocks = ('MSFT', 'TSLA', 'GOOG', 'AAPL', 'NVDA')

# Aplicación
st.title('Stock Forecast App')
st.divider()

################################
# Filtros y criterios
################################

selected_stock = st.selectbox('Select a stock: ', stocks)
n_years = st.slider('Years of predicrion: ', 1, 4)

period = n_years * 365

################################
# Data cruda 
################################

st.subheader('Raw Data')

#  Cargamos la data
df = load_data(selected_stock, START, TODAY)
st.write(df.tail())

# Visualización de la data
fig = plot_raw_data(df)
st.plotly_chart(fig)

################################
# Predicción
################################

df_train = df[['Date', 'Close']]
df_train = df_train.rename(columns={
    'Date': 'ds',
    'Close': 'y'
})


# Entrenamiento del modelo
model = Prophet()
model.fit(df_train)

future = model.make_future_dataframe(periods=period)
forecast = model.predict(future)

# Visualización de la predicción
st.subheader('Forecast Data')

# Data 
st.write(forecast.tail())

# Serie de tiempo
st.write(f'**Forecast plot for {n_years} years**')
fig1 = plot_plotly(model, forecast)
st.plotly_chart(fig1)

# Componentes 
st.write('**Forecast Components**')
# fig2 = model.plot_components(forecast)
fig2 = plot_components_plotly(model, forecast)
st.plotly_chart(fig2)