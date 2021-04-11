from pandas_datareader.data import DataReader
from datetime import date
import matplotlib.pyplot as plt

series_code = 'DGS10'  # 10-year Tresury Date
series_name = '10-year Treasury'
data_source = 'fred'  # FED Economic Data Service
start = date(1962, 1, 1)

data = DataReader(series_code, data_source, start)

print(data.info())

data = data.rename(columns={series_code: series_name})
data.plot(title=series_name)
plt.show()