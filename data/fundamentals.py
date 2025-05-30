import os
import requests
from dotenv import load_dotenv

load_dotenv()
FINNHUB_API_KET = os.getenv("FINN_API_KEY")

def get_financial_ratios(ticker):
    base_url = "https://"