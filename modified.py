import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

def main():
    st.write("# Stock Price Analyzer")
    st.write("Shown are stock prices of companies.")

    ticker_symbol = st.text_input("Enter stock symbol", "AAPL", key="ticker_input")

    ticker_data = yf.Ticker(ticker_symbol)

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Enter start date of stock", datetime.date(2019, 1, 1))
    with col2:
        end_date = st.date_input("Enter end date of stock", datetime.date(2023, 8, 23))

    ticker_df = get_ticker_data(ticker_data, start_date, end_date)

    st.write(f"### {ticker_symbol}'s End-of-Day Price Table")
    st.dataframe(ticker_df)

    plot_line_chart(ticker_df.Close, f"{ticker_symbol}'s Daily Price Closing Chart")
    plot_line_chart(ticker_df.Volume, f"{ticker_symbol}'s Daily Volume Traded Chart")

def get_ticker_data(ticker_data, start_date, end_date):
    ticker_df = ticker_data.history(period="1d", start=start_date, end=end_date)
    return ticker_df

def plot_line_chart(data, title):
    st.write(f"### {title}")
    st.line_chart(data)

if __name__ == "__main__":
    main()
