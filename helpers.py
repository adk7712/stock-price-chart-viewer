import yfinance as yf

def lookup(symbol, period):
    # Choose highest-detail interval based on period
    if period == "1d":
        yf_interval = "1m"
    elif period in ["5d", "1w"]:
        yf_interval = "5m"
        period = "5d"
    elif period in ["1mo", "3mo", "6mo"]:
        yf_interval = "60m"
    elif period in ["1y", "2y"]:
        yf_interval = "1d"
    elif period in ["5y", "10y"]:
        yf_interval = "1wk"
    elif period == "max":
        yf_interval = "1mo"
    else:
        return None

    PERIOD_LABELS = {
        "1d": "Intraday Chart",
        "1w": "1-Week Chart",
        "5d": "5-Day Chart",
        "1mo": "1-Month Chart",
        "3mo": "3-Month Chart",
        "6mo": "6-Month Chart",
        "1y": "1-Year Chart",
        "2y": "2-Year Chart",
        "5y": "5-Year Chart",
        "10y": "10-Year Chart",
        "max": "Max History Chart"
    }

    # Download data
    data = yf.download(symbol, period=period, interval=yf_interval, progress=False)

    prices = []
    labels = []

    if data is not None and not data.empty:
        for value in data["Close"].values.tolist():
            if isinstance(value, list):
                prices.append(value[0])
            else:
                prices.append(value)

        for date in data.index:
            if yf_interval in ["1m", "5m", "15m", "30m", "60m"]:
                labels.append(date.strftime('%Y-%m-%d %H:%M'))
            else:
                labels.append(date.strftime('%Y-%m-%d'))
    else:
        print("No data")

    try:
        info = {
            "symbol": symbol,
            "name": yf.Ticker(symbol).info["longName"],
            "period": PERIOD_LABELS[period],
            "prices": prices,
            "labels": labels
        }
    except KeyError:
        info = None

    return info
