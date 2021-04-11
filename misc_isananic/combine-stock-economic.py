from pandas_datareader.data import DataReader
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt


start = date(2000, 1, 1)

# Economic Data: Fed Economic Data - fred
# Other series: GOLDAMGBD228NLBM - Gold
#               UNRATE - Civilian Uneployment Rate
#               CIVPART - Civilian Labor Force Participation Rate
#               BAMLHYH0A0HYM2TRIV - Bank of America Merril lynch US High Yield total Return Index value
#               SP500 - SP500 Index (Very correlated with previous)
series = 'DCOILWTICO'  # West texas Intermediate Oil Price
oil = DataReader(series, 'fred', start)  # Note, series can be a list

# Exxom Mobile Data
ticker = 'XOM'  # Exxom Mobile
stock = DataReader(ticker, 'yahoo', start)

data = pd.concat([stock[['Close']], oil], axis = 1)
data.columns = ['Exxon', 'Oil Price']

print(data.info())

data.plot() # If plotting several columns with subplots=true, prints several axis
plt.show()