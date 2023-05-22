import streamlit as st
import yfinance as yf
import pandas as pd
import datetime


st.title('Stock Market Analysis')
st.write('This is my first app')

inputer=st.text_input("Enter Stock Name", "MSFT", key="placeholder")

ticker_symbol=inputer
ticker_data = yf.Ticker(ticker_symbol)



col1, col2= st.columns(2)

with col1:
    sd = st.date_input(
        "Enter Starting Date",
        datetime.date(2019, 1, 1))

with col2:
    ed = st.date_input(
        "Enter Closing Date",
        datetime.date(2022, 5, 21))




# get historical market data
ticker_df = ticker_data.history(period="1d",
                                start=f"{sd}",
                                end=f"{ed}")

st.write( f"We are viewing info for {ticker_symbol}")

st.write(ticker_df)

#st.dataframe(ticker_df)
#Using a line chart to represent Volumne


col1, col2= st.columns(2)

with col1:
    st.write("Volume Analysis")
    st.line_chart(ticker_df['Volume'])

with col2:
    st.write("Closing Price Analysis")
    st.line_chart(ticker_df['Close'])




