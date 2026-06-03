# app.py - Vydavky na webe (Projekt 4). Vrstva OBSLUHA pre web (namiesto terminaloveho menu).
# Pouziva tie iste vrstvy ako terminalova appka: databaza.py a konfig.py.
# Spustenie:  python app.py    (potom otvor http://127.0.0.1:5000) ;  zastavenie: Ctrl+C

from flask import Flask, render_template

import databaza
import konfig

app = Flask(__name__)


@app.route("/")
def domov():
    # Vezmeme data z TEJ ISTEJ vrstvy databaza.py, co pouziva terminalova appka.
    conn = databaza.pripoj()
    databaza.vytvor_tabulku(conn)
    vydavky = databaza.vsetky_vydavky(conn)
    conn.close()
    # render_template dosadi data do HTML sablony templates/vydavky.html
    return render_template("vydavky.html", vydavky=vydavky, mena=konfig.MENA)


if __name__ == "__main__":
    app.run(debug=True)
