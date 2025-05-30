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