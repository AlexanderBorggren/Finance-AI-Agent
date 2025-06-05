from application.processor import process_ticker_list, fetch_all_data
from config.settings import API_SOURCE

if __name__ == "__main__":

    tickers = fetch_all_data(["US", "ST"])
    ranked = process_ticker_list(tickers, API_SOURCE)
    print(f"Antal tickers hämtade: {len(tickers)}")

    for stock in ranked[:10]:
        print(f"{stock['ticker']}: Magic Score = {stock['magic_score']}, ROIC = {stock['return_on_capital']}%, EY = {stock['earnings_yield']}%")