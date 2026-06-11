# api_demo.py - Projekt 9, Etapa 1: tvoj VLASTNY API (Flask vracia JSON, nie HTML).
# Endpoint /api/scitaj?a=2&b=3 vrati JSON s vysledkom.
# Spustenie:  python api_demo.py   (potom skus http://127.0.0.1:5002/api/scitaj?a=2&b=3)

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route("/")
def domov():
    """Stranka so scitanim - pouzije JavaScript (fetch) na zavolanie nasho API."""
    return render_template("scitanie.html")


@app.route("/api/scitaj")
def api_scitaj():
    """Vrati SUCET dvoch cisel ako JSON. Cisla pridu ako parametre v adrese (?a=..&b=..)."""
    try:
        a = float(request.args.get("a", ""))
        b = float(request.args.get("b", ""))
    except ValueError:
        # 400 = "zla poziadavka" (Bad Request) + JSON s chybou
        return jsonify({"chyba": "Zadaj dve platne cisla v parametroch a a b."}), 400
    return jsonify({"a": a, "b": b, "sucet": a + b})


if __name__ == "__main__":
    # Port 5002, aby sa nehadal s vydavkami (5000) ani pocasim (5001).
    app.run(debug=True, port=5002)
