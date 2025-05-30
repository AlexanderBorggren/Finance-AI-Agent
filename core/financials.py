def calculate_metrics(fundamental_data: dict) -> dict:
    income = fundamental_data["income"]
    balance = fundamental_data["balance"]

    ebit = float(income.get("operatingIncome", 0))
    ca = float(balance.get("totalCurrentAssets", 0))
    cl = float(balance.get("totalCurrentLiabilities", 0))
    nwc = ca - cl
    ppe = float(balance.get("propertyPlantEquipmentNet", 0))
    capital = nwc + ppe

    debt = float(balance.get("totalDebt", 0))
    cash = float(balance.get("cashAndCashEquivalents", 0))

    market_cap = fundamental_data.get("market_cap", 0)

    ev = market_cap + debt - cash if market_cap else 0
    earnings_yield = ebit / ev if ev else 0
    return_on_capital = ebit / capital if capital else 0

    return {
        "ticker": fundamental_data["ticker"],
        "ebit": ebit,
        "ev": ev,
        "capital": capital,
        "earnings_yield": earnings_yield,
        "return_on_capital": return_on_capital
    }