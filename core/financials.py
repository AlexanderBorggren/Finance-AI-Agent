def calculate_metrics(fundamental_data: dict) -> dict:
    ticker = fundamental_data.get("ticker")
    profile = fundamental_data.get("profile", {})
    quote = fundamental_data.get("quote", {})
    metrics = fundamental_data.get("financials", {})

    eps = metrics.get("epsTTM")
    price = quote.get("c")
    ebitda_per_share = metrics.get("ebitdPerShareTTM")
    book_value_per_share = metrics.get("bookValuePerShareAnnual")
    shares_outstanding = profile.get("shareOutstanding")
    debt_to_equity = metrics.get("totalDebt/totalEquityAnnual")

    if None in (eps, price, ebitda_per_share, book_value_per_share, shares_outstanding, debt_to_equity):
        return {"ticker": ticker, "error": "Insufficient data"}

    depreciation = 0.10 * ebitda_per_share
    ebit_per_share = ebitda_per_share - depreciation
    ebit = ebit_per_share * shares_outstanding

    equity = book_value_per_share * shares_outstanding
    debt = debt_to_equity * equity
    invested_capital = equity + debt
    ev = fundamental_data.get("quote", {}).get("c", 0) * shares_outstanding + debt

    tax_rate = 0.21
    nopat = ebit * (1 - tax_rate)
    earnings_yield = (eps / price) * 100 if price else 0
    roic = (nopat / invested_capital) * 100 if invested_capital else 0

    return {
        "ticker": ticker,
        "ebit": round(ebit, 2),
        "ev": round(ev, 2),
        "capital": round(invested_capital, 2),
        "earnings_yield": round(earnings_yield, 2),
        "return_on_capital": round(roic, 2)
    }