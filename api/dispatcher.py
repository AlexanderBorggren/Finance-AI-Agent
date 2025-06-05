import importlib
from api.sources.sources_enum import ApiSource

def fetch_fundamentals(ticker: str, source: ApiSource) -> dict:
    module = importlib.import_module(source.handler)

    if source.use_sdk and hasattr(module, "fetch_company_data_sdk"):
        return module.fetch_company_data_sdk(ticker)
    elif hasattr(module, "fetch_company_data"):
        return module.fetch_company_data(ticker, base_url=source.base_url)
    else:
        raise NotImplementedError(f"{source.label} saknar funktion för fetch_company_data")

def fetch_all_tickers(source: ApiSource, exchanges: list[str]) -> list[str]:
    module = importlib.import_module(source.handler)

    ticker_function = None
    if source.use_sdk and hasattr(module, "fetch_tickers_sdk"):
        ticker_function = module.fetch_tickers_sdk
    else:
        raise NotImplementedError(f"{source.label} saknar funktion för fetch_tickers")

    tickers = []
    for exchange in exchanges:
        tickers.extend(ticker_function(exchange))

    return tickers