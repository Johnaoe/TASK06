import yfinance as yf

tickers = yf.Tickers('aapl')
df = tickers.tickers.AAPL.history(period="1mo")
df.reset_index(inplace=True)
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
df.drop(['Dividends','Stock Splits'], inplace=True, axis=1)
df.to_dict(orient='records')