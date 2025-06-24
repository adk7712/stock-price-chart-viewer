# Stock Price Chart Viewer

#### Video Demo: [Watch on YouTube](https://youtu.be/euDbxCAzH3o)

---

**Stock Price Chart Viewer** is a lightweight, fast, and interactive web application for visualizing stock prices across multiple time periods. Whether you're a casual investor, student, or just curious about market trends, this tool provides a clean and simple way to view how stock prices have evolved over time — all powered by real-time financial data from Yahoo Finance.

---

<img src="docs/preview.png" alt="Preview of Stock Price Chart Viewer">

---

## Features

- Stock Lookup: Search by stock ticker (e.g., `AAPL`, `GOOG`, `MSFT`) to fetch real-time market data.
- Time Period Selection: Choose from a wide range of periods to analyze stock performance:
  - 1 Day, 1 Week, 1 Month, 3 Months, 6 Months, 1 Year, 2 Years, 5 Years, 10 Years, Max
- Interactive Charts: Smooth and responsive line charts powered by Chart.js.
- Dark Mode UI: A modern and sleek dark-themed interface for better readability.
- Auto-adjusted Granularity: Chart interval adapts to selected period (e.g., minute-level for 1 day, daily for years).
- Fast Loading: Minimal and optimized backend for quick data fetching and rendering.

---

## Tech Stack

| Layer     | Technology                                   |
|-----------|----------------------------------------------|
| Backend   | [Python](https://www.python.org), [Flask](https://flask.palletsprojects.com) |
| Frontend  | [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML), [Bootstrap 5](https://getbootstrap.com), [Chart.js](https://www.chartjs.org) |
| Data API  | [yfinance](https://github.com/ranaroussi/yfinance) (Yahoo Finance wrapper) |

---

## Getting Started

1. Clone this repository
  ```bash

git clone https://github.com/adk7712/stock-price-chart-viewer
cd stock-price-chart-viewer

  ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app

```bash
flask run
```

4. Go to this url in your browser to view project: http://127.0.0.1:5000

## TODO / Improvements

- Add candlestick chart option
- Add volume indicators
- Add historical news data per date
- Deploy to a cloud platform (Render, Vercel, etc.)

## License

MIT License


## Credits

- Chart.js
- yfinance
- Bootstrap
