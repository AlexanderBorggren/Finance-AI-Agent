def rank_stocks(metrics_list: list[dict]) -> list[dict]:
    sorted_by_roc = sorted(metrics_list, key=lambda x: x["return_on_capital"], reverse=True)
    for i, entry in enumerate(sorted_by_roc):
        entry["roc_rank"] = i + 1

    sorted_by_ey = sorted(metrics_list, key=lambda x: x["earnings_yield"], reverse=True)
    for i, entry in enumerate(sorted_by_ey):
        entry["ey_rank"] = i + 1

    ranked = sorted(metrics_list, key=lambda x: x["magic_score"])
    return ranked
