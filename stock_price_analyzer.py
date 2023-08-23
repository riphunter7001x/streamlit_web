import pandas as pd
import streamlit as st
import yfinance as yf
import datetime


# wite heading 

st.write(
         """
        #  stock price analyzer
        
        shown are stock price company's
        """ 
         )

# lest take input from user which stock want to analze

ticker_symobol = st.text_input("enter stock symobol",
                               "aapl",
                               key = "placeholder")

ticker_data = yf.Ticker(ticker_symobol)
# lets ask  user date he want to start

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("enter start date of stock ",
                datetime.date(2019,1,1)                 )
with col2:
    end_date = st.date_input("enter end date of stock ",
                datetime.date(2023,8,23)              )

ticker_df = ticker_data.history(period="1d",
                                 start = start_date,
                                 end =end_date
                                 )
st.write(f"""
        ### {ticker_symobol}'s EOD price table
         """)   
st.dataframe(ticker_df)



# lets plot line chat 
st.write(
        """
         daily price closing chart
         
         """)
st.line_chart(ticker_df.Close)

st.write("""
         daily volume traded chart
         
         """)
st.line_chart(ticker_df.Volume)