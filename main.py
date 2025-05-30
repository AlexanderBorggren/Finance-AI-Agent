from api.dispatcher import fetch_fundamentals
from config.settings import API_SOURCE

if __name__ == "__main__":

    tickers_data = [
       {"ticker": "AAPL"},
       {"ticker": "MSFT"},
       {"ticker": "GOOGL"}
    ]

    for ticker in tickers_data:
        result = fetch_fundamentals(ticker, API_SOURCE)

    print(result)