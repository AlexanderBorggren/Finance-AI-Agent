import os
from dotenv import load_dotenv
import finnhub


load_dotenv()
API_KEY = os.getenv("FINNHUB_API_KEY")
finnhub_client = finnhub.Client(api_key=API_KEY)

def fetch_company_data_sdk(ticker: str) -> dict:
    try:
        profile = finnhub_client.company_profile2(symbol=ticker)
        quote = finnhub_client.quote(ticker)
        financials = finnhub_client.company_basic_financials(ticker, 'all')
        return {
            "ticker": ticker,
            "profile": profile,
            "quote": quote,
            "financials": financials.get("metric", {})
        }
    except Exception as e:
        print(f"Fel vid hämtning av data för {ticker}: {e}")
        return {}
    

def fetch_tickers_sdk(exchange: str) -> list[str]:
    try:
        data = finnhub_client.stock_symbols(exchange)
        return [item["symbol"] for item in data if item.get("type") == "Common Stock"]
    except Exception as e:
        print(f"Fel vid hämtning av tickers från börs {exchange}: {e}")
        return []