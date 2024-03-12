from pytickersymbols import PyTickerSymbols

# Initialize the PyTickerSymbols object
stock_data = PyTickerSymbols()

# Get all FTSE 100 stocks
uk_stocks = stock_data.get_stocks_by_index('FTSE 100')

# Print the list of FTSE 100 stock tickers
print("FTSE 100 Tickers:")
for stock in uk_stocks:
    print(stock)
