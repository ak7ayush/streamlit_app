import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Stock Market App")

st.write("This is my hope of getting hike")

ticker_data = yf.Ticker('AAPL')

hist = ticker_data.history(start='2022-05-31', end='2022-07-30')

st.write("I'm going to show apple data")

st.write(hist)

st.write('This is volume of stock')
st.line_chart(hist.Volume)
