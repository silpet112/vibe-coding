# web_pocasie.py - Projekt 6, Etapa 4: pocasie na webe (Flask).
# Znova pouziva funkcie z pocasie.py (najdi_mesto, stiahni_pocasie, popis_pocasia)
# - rovnaka logika pre terminal aj web (sila oddelenych vrstiev).
# Spustenie:  python web_pocasie.py   (potom otvor http://127.0.0.1:5001)

from flask import Flask, render_template, request
import requests

import pocasie  # znova pouzite funkcie z terminalovej verzie

app = Flask(__name__)


@app.route("/")
def domov():
    nazov = request.args.get("mesto", "").strip()  # mesto z adresy (?mesto=...)
    vysledok = None
    chyba = None
    if nazov:
        try:
            mesto = pocasie.najdi_mesto(nazov)
            if mesto is None:
                chyba = f"Mesto '{nazov}' som nenašiel, skús iný názov."
            else:
                data = pocasie.stiahni_pocasie(mesto["latitude"], mesto["longitude"])
                c = data["current"]
                vysledok = {
                    "mesto": mesto["name"],
                    "krajina": mesto.get("country", ""),
                    "teplota": c["temperature_2m"],
                    "pocit": c["apparent_temperature"],
                    "stav": pocasie.popis_pocasia(c["weather_code"]),
                    "emoji": pocasie.emoji_pocasia(c["weather_code"]),
                    "predpoved": pocasie.predpoved_z_dat(data),
                }
        except requests.exceptions.RequestException as e:
            # Zapiseme skutocnu chybu do logov (uzitocne pri ladeni nasadenej appky),
            # pouzivatelovi ukazeme zrozumitelnu hlasku.
            print("CHYBA API:", type(e).__name__, "-", e, flush=True)
            chyba = "Služba počasia má práve dočasný výpadok. Skús to o chvíľu znova."
    return render_template("pocasie.html", nazov=nazov, vysledok=vysledok, chyba=chyba)


if __name__ == "__main__":
    # Port 5001, aby sa nehadal s vydavkovou appkou (tá beží na 5000).
    app.run(debug=True, port=5001)
