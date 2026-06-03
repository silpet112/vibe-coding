# app.py - Vydavky na webe (Projekt 4). Vrstva OBSLUHA pre web (namiesto terminaloveho menu).
# Pouziva tie iste vrstvy ako terminalova appka: databaza.py, logika.py a konfig.py.
# Spustenie:  python app.py    (potom otvor http://127.0.0.1:5000) ;  zastavenie: Ctrl+C

import os
import threading
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
    # Filter z adresy (query string), napr. /?kategoria=jedlo. Prazdny = vsetky.
    filter_kat = request.args.get("kategoria", "").strip()
    if filter_kat:
        vydavky = databaza.vydavky_v_kategorii(conn, filter_kat)
    else:
        vydavky = databaza.vsetky_vydavky(conn)
    # Prehlady (vzdy za vsetko) - znova pouzite funkcie z Projektu 3 (databaza.py).
    spolu = databaza.sucet_vsetkych(conn)
    podla_kategorie = databaza.sucet_podla_kategorie(conn)
    conn.close()
    # render_template dosadi data do HTML sablony templates/vydavky.html
    return render_template(
        "vydavky.html",
        vydavky=vydavky,
        spolu=spolu,
        podla_kategorie=podla_kategorie,
        mena=konfig.MENA,
        filter_kat=filter_kat,
    )


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


@app.route("/zmaz/<int:id_vydavku>", methods=["POST"])
def zmaz(id_vydavku):
    # <int:id_vydavku> = cislo z adresy (napr. /zmaz/3) sa odovzda funkcii.
    conn = databaza.pripoj()
    databaza.zmaz_vydavok(conn, id_vydavku)
    conn.close()
    return redirect(url_for("domov"))


@app.route("/uprav/<int:id_vydavku>", methods=["GET", "POST"])
def uprav(id_vydavku):
    conn = databaza.pripoj()
    databaza.vytvor_tabulku(conn)
    if request.method == "POST":
        # Krok 2: ulozit zmenu (SQL UPDATE).
        suma = logika.parsuj_sumu(request.form.get("suma", ""))
        if suma is not None:
            kategoria = request.form.get("kategoria", "").strip() or "ine"
            zadany_datum = request.form.get("datum", "").strip()
            datum = zadany_datum if zadany_datum else str(date.today())
            poznamka = request.form.get("poznamka", "").strip()
            databaza.uprav_vydavok(conn, id_vydavku, suma, kategoria, datum, poznamka)
        conn.close()
        return redirect(url_for("domov"))
    # Krok 1 (GET): zobrazit formular s predvyplnenymi hodnotami.
    v = databaza.vydavok_podla_id(conn, id_vydavku)
    conn.close()
    if v is None:  # taky vydavok neexistuje -> spat na zoznam
        return redirect(url_for("domov"))
    return render_template("uprav.html", v=v, mena=konfig.MENA)


@app.route("/vypni", methods=["POST"])
def vypni():
    # Naplanuje vypnutie servera tesne po odoslani odpovede (aby sa stranka stihla zobrazit).
    # os._exit ukonci proces (aj s Flask reloaderom).
    threading.Timer(0.5, lambda: os._exit(0)).start()
    return "<h1>Server je vypnutý 🛑</h1><p>Túto kartu môžeš zatvoriť. Znova ho spustíš cez /app.</p>"


if __name__ == "__main__":
    app.run(debug=True)
