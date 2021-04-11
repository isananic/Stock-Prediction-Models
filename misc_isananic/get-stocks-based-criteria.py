# Excel method
# nyse = pd.read_excel('listings.xlsx', sheetname = 'nyse', na_values='n/a')
# nyse = nyse.sort_values('Market Capitalization', ascending=False)
# nyse[['Stock Symbol', 'Company Name']].head(3)

# More elegant way
# nyse = nyse.set_index('Stock Symbol')  # Stock ticker as index
# nyse.info()
# nyse['Market Capitalization`].idxmax() # Returns ticker(idx) of highest capitalization

# nyse['Sector'].unique()
# tech = nyse.loc[nyse.Sector == 'Technology']
# tech['Company Name'].head(2)
# nyse.loc[nyse.Sector=='Technology', 'Market Capitalization'].idxmax()

# Observe, the nyse (listings.xlsx) contains the listing information
# ticker = nyse.loc[(nyse.Sector=='Technology') & (nyse['IPO Year']==2017), 'Market Capitalization'].idxmax()
# data = DataReader(ticker, 'yahoo') # start 2010,1,1
# data = data.loc[:, ['Close', 'Volume']]

# Plot two measures with different Y in the same graph:
# import matplotlib.pyplot as plt
#
# data.plot(title=ticker, secondary_y='Volume')
# plt.tight_layout()