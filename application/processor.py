from api.dispatcher import fetch_fundamentals, fetch_all_tickers
from api.sources.sources_enum import ApiSource
from core.financials import calculate_metrics
from core.magic_formula import rank_stocks
from config.settings import API_SOURCE


def process_ticker(ticker: str, source: ApiSource) -> dict:
    fundamentals = fetch_fundamentals(ticker, source)
    return calculate_metrics(fundamentals)

def process_ticker_list(tickers: list[str], source: ApiSource) -> list[dict]:
    metrics_list = []

    for ticker in tickers:
        data = process_ticker(ticker, source)
        if "error" not in data:
            metrics_list.append(data)

    return rank_stocks(metrics_list)

def fetch_all_data(exchanges: list[str] = ["US", "ST"]) -> list[str]:
    return fetch_all_tickers(API_SOURCE, exchanges)

