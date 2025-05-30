from api.dispatcher import fetch_fundamentals
from api.sources.sources_enum import ApiSource
from core.financials import calculate_metrics

def process_ticker(ticker: str, source: ApiSource) -> dict:
    fundamentals = fetch_fundamentals(ticker, source)
    return calculate_metrics(fundamentals)