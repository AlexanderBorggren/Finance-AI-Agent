import os
from dotenv import load_dotenv
import finnhub


load_dotenv()
API_KEY = os.getenv("FINNHUB_API_KEY")
finnhub_client = finnhub.Client(api_key=API_KEY)

def fetch_fundamentals_sdk(ticker: str) -> dict:  
    try:
        print(API_KEY)
        print(f"Fetching income statement for {ticker}")
        income_data = finnhub_client.financials(ticker, 'ic', 'annual')["data"][0]
        balance_data = finnhub_client.financials(ticker, 'bs', 'annual')["data"][0]

        return {
            "ticker": ticker,
            "income": income_data,
            "balance": balance_data
        }
    except Exception as e:
        print(f"Error for {ticker}: {e}")
        return {}