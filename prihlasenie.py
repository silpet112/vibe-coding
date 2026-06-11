# prihlasenie.py - Projekt 10, Etapa 2: prihlasenie/odhlasenie + session.
# Heslo overujeme cez hash (Etapa 1). Session = appka si pamata prihlaseneho pouzivatela.
# Spustenie:  python prihlasenie.py   (potom http://127.0.0.1:5003)

from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# Tajny kluc je potrebny pre session. V realnej appke by patril do .env!
app.secret_key = "tajny-kluc-len-na-ucenie"

# Demo pouzivatelia: meno -> HASH hesla (nikdy nie heslo v texte).
POUZIVATELIA = {
    "admin": generate_password_hash("tajne123"),
}


@app.route("/")
def domov():
    # session.get vrati meno prihlaseneho, alebo None ak nikto nie je prihlaseny.
    return render_template("prihlasenie.html", pouzivatel=session.get("pouzivatel"), chyba=None)


@app.route("/prihlas", methods=["POST"])
def prihlas():
    meno = request.form.get("meno", "").strip()
    heslo = request.form.get("heslo", "")
    hash_hesla = POUZIVATELIA.get(meno)
    # over: pouzivatel existuje A heslo sedi s ulozenym hashom
    if hash_hesla and check_password_hash(hash_hesla, heslo):
        session["pouzivatel"] = meno          # zapamatame si prihlasenie
        return redirect(url_for("domov"))
    return render_template("prihlasenie.html", pouzivatel=None,
                           chyba="Nesprávne meno alebo heslo.")


@app.route("/odhlas")
def odhlas():
    session.pop("pouzivatel", None)           # zabudni prihlasenie
    return redirect(url_for("domov"))


if __name__ == "__main__":
    app.run(debug=True, port=5003)
