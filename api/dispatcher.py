from api.sources.sources_enum import ApiSource
import importlib

def fetch_fundamentals(ticker: str, source: ApiSource) -> dict:
    module = importlib.import_module(source.handler)
    
    if source.use_sdk:
        return module.fetch_company_data_sdk(ticker)
    else:
        return module.fetch_company_data(ticker, base_url=source.base_url)
    