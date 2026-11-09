import pandas as pd 
import numpy as np 
import yfinance as yf 

# Descargar precios desde yahoo finance
tickers = ["IVV", "ILF", "SOXX"] # SP500, LATAM, Semiconductores (IA)
vector_w = [0.5,0.3,0.2]
vector_w = np.array(vector_w).reshape(-1,1)
df_prices = yf.download(tickers, start="2024-01-01", end="2026-09-30")["Close"]

#calcular retornos diarios
df_ret = df_prices.pct_change().dropna()


#calcular matriz varianza covarianza
df_cov = df_ret.cov()

#Calcular varianza del portafolio
w = vector_w
w_t = w.T
sigma = df_cov.values

print("w", w.shape)
print("w_t", w_t.shape)
print("sigma", sigma.shape)

varianza = np.dot(sigma, w)
varianza = np.dot(w_t, varianza)
varianza = varianza[0] [0]

#Calcular Desviación Estándar
desv = varianza**(1/2)
volatilidad_anual = desv * 252**(1/2)
print(f"La volatilidad del portafolio es: {volatilidad_anual*100:.04}%")

