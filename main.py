from application.processor import process_ticker_list
from config.settings import API_SOURCE

if __name__ == "__main__":


    tickers = ["MSFT", "AAPL", "GOOGL"]
    ranked = process_ticker_list(tickers, API_SOURCE)

    for stock in ranked:
        print(f"{stock['ticker']}: Magic Score = {stock['magic_score']}, ROIC = {stock['return_on_capital']}%, EY = {stock['earnings_yield']}%")