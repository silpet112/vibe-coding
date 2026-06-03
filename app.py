# app.py - Vydavky na webe (Projekt 4), Etapa 1: prva webova stranka cez Flask.
# Spustenie:  python app.py    (potom otvor v prehliadaci http://127.0.0.1:5000)
# Zastavenie servera v termini: Ctrl+C

from flask import Flask

# Vytvorime webovu aplikaciu.
app = Flask(__name__)


# "Route" = ked pride poziadavka na adresu "/", spusti tuto funkciu a vrat jej vysledok.
@app.route("/")
def domov():
    return "<h1>Ahoj! Toto je moja prva webova stranka. 🎉</h1><p>Bezi na mojom pocitaci cez Flask.</p>"


if __name__ == "__main__":
    # Spusti vyvojovy web server. debug=True = pri zmene kodu sa sam restartuje a ukazuje chyby.
    app.run(debug=True)
