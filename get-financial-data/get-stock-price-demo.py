from pandas_datareader.data import DataReader
from datetime import date  # Date & Time functionality
import pandas as pd
import matplotlib.pyplot as plt

# Stock we want to get
stock_name = 'Google'
start = date(2015, 1, 1)
end = date(2021, 4, 9)
data_source = 'yahoo' # Yahoo finance

# Ticker map
ticker_map = {'Google': 'GOOG',
              'Twilio': 'TWLO',
              'Teradata': 'TDC',
              'Volkswagen': 'VOW.DE',
              'Apple': 'AAPL',
              'Bandwidth': 'BAND',
              'Oryzon': 'ORY.MC'}
ticker = ticker_map.get(stock_name, 'Ticker not found')

# stock_data object
stock_data = DataReader(ticker, data_source, start, end)

# Info available on stock
# stock_data.info()
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   High       1578 non-null   float64 - High value
#  1   Low        1578 non-null   float64 - Low value
#  2   Open       1578 non-null   float64 - Open value
#  3   Close      1578 non-null   float64 - Close value
#  4   Volume     1578 non-null   float64 - Volume
#  5   Adj Close  1578 non-null   float64

# Display the dataset content
print(pd.concat([stock_data.head(3), stock_data.tail(3)]))

stock_data['Close'].plot(title=ticker)
plt.show()