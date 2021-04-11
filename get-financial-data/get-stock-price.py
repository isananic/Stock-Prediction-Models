from pandas_datareader.data import DataReader
from datetime import date, timedelta  # Date & Time functionality


def get_stock_price(stock_name, start=date.today() - timedelta(30), end=date.today(), data_source='yahoo'):
    """This function gets the information about the stock_name we provide,
        * By default, it downloads the last 30 days of data
        * By default it uses 'yahoo' asa data source
        * Data Sources: yahoo, iex
        * NOTE: Iex returns column-names in lowercase --> automatically change always to lowercase
    Example Use:
        get_stock_price('Google', start=date(2015,1,1))"""

    # Ticker map
    ticker_map = {'Google': 'GOOG',
                  'Twilio': 'TWLO',
                  'Teradata': 'TDC',
                  'Volkswagen': 'VOW.DE',
                  'Apple': 'AAPL',
                  'Bandwidth': 'BAND',
                  'Oryzon': 'ORY.MC'}
    ticker = ticker_map.get(stock_name, 'Ticker not found')

    # stock_data object: High, Low, Open, Close, Volume, Adj Close  (float64) // Close|Volume
    stock_price_df = DataReader(ticker, data_source, start, end)
    stock_price_df.columns = stock_price_df.columns.str.lower()

    return stock_price_df
