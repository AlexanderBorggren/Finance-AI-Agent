from data.market import get_market_tickers
from core.magic_formula import score_stocks

def run_weekly_report():
    tickers = get_market_tickers()
    ranked = score_stocks(tickers)

    print("\nVeckans toppval enligt Magic Formula:\n")
    for stock in ranked[:3]:
        print(f"{stock['ticker']}: ROIC={stock['roic']}%, EY={stock['ey']}%, Score={stock['score']}")