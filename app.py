from flask import Flask, render_template, request
from helpers import lookup

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    symbol = str(request.args.get("symbol", "AAPL")).upper()
    period = str(request.args.get("period", "1w")).lower()

    info = lookup(symbol, period)

    if info == None:
        return render_template("error.html")

    return render_template("index.html", info=info, symbol=symbol, period=period)
