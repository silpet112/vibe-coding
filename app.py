# app.py - Vydavky na webe (Projekt 4). Vrstva OBSLUHA pre web (namiesto terminaloveho menu).
# Pouziva tie iste vrstvy ako terminalova appka: databaza.py, logika.py a konfig.py.
# Spustenie:  python app.py    (potom otvor http://127.0.0.1:5000) ;  zastavenie: Ctrl+C

from datetime import date

from flask import Flask, render_template, request, redirect, url_for

import databaza
import konfig
import logika

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


@app.route("/pridaj", methods=["POST"])
def pridaj():
    # request.form = data odoslane z formulara (metoda POST).
    suma = logika.parsuj_sumu(request.form.get("suma", ""))
    if suma is not None:  # neplatnu sumu jednoducho ignorujeme
        kategoria = request.form.get("kategoria", "").strip() or "ine"
        zadany_datum = request.form.get("datum", "").strip()
        datum = zadany_datum if zadany_datum else str(date.today())
        poznamka = request.form.get("poznamka", "").strip()
        conn = databaza.pripoj()
        databaza.vytvor_tabulku(conn)
        databaza.pridaj_vydavok(conn, suma, kategoria, datum, poznamka)
        conn.close()
    # Presmerovanie spat na zoznam (aby sa F5 neodoslalo formular znova).
    return redirect(url_for("domov"))


if __name__ == "__main__":
    app.run(debug=True)
