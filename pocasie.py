# pocasie.py - Projekt 6, Etapa 3: krajsi vypis (pocitova teplota + slovny popis) + osetrenie chyb.
# Dve volania API: 1) geocoding (mesto -> suradnice)  2) forecast (suradnice -> pocasie).
# Open-Meteo: https://open-meteo.com  (netreba API kluc)

from datetime import datetime

import requests

# Slovenske nazvy dni (0 = pondelok, ako date.weekday()).
DNI_V_TYZDNI = ["Pondelok", "Utorok", "Streda", "Štvrtok", "Piatok", "Sobota", "Nedeľa"]

# Emoji ku kazdemu stavu pocasia (zrozumitelne aj bez slovenciny).
EMOJI_POCASIA = {
    0: "☀️", 1: "🌤️", 2: "⛅", 3: "☁️",
    45: "🌫️", 48: "🌫️",
    51: "🌦️", 53: "🌦️", 55: "🌦️",
    61: "🌧️", 63: "🌧️", 65: "🌧️",
    71: "❄️", 73: "❄️", 75: "❄️",
    80: "🌦️", 81: "🌦️", 82: "🌧️",
    95: "⛈️",
}

# Preklad "weather_code" (cislo stavu pocasia od Open-Meteo) na slovensky popis.
POPISY_POCASIA = {
    0: "jasno",
    1: "prevazne jasno",
    2: "polojasno",
    3: "zamracene",
    45: "hmla",
    48: "namrzajuca hmla",
    51: "slabe mrholenie",
    53: "mrholenie",
    55: "silne mrholenie",
    61: "slaby dazd",
    63: "dazd",
    65: "silny dazd",
    71: "slabe snezenie",
    73: "snezenie",
    75: "silne snezenie",
    80: "dazdove prehanky",
    81: "prehanky",
    82: "silne prehanky",
    95: "burka",
}


# --- Praca s API ---

def najdi_mesto(nazov):
    """Cez geocoding API zisti udaje o meste. Vrati slovnik prveho vysledku, alebo None."""
    odpoved = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": nazov, "count": 1, "language": "sk", "format": "json"},
        timeout=10,
    )
    odpoved.raise_for_status()
    vysledky = odpoved.json().get("results")
    if not vysledky:
        return None
    return vysledky[0]


def stiahni_pocasie(lat, lon):
    """Vrati aktualne pocasie + 7-dnovu predpoved ako slovnik.
    timezone=auto -> datumy a casy su v miestnom case daneho mesta."""
    odpoved = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,apparent_temperature,weather_code",
            "daily": "weather_code,temperature_2m_max,temperature_2m_min",
            "forecast_days": 7,
            "timezone": "auto",
        },
        timeout=10,
    )
    odpoved.raise_for_status()
    return odpoved.json()


# --- Cista logika (da sa testovat bez internetu) ---

def teplota_z_dat(data):
    """Z odpovede (slovnik) vytiahne aktualnu teplotu."""
    return data["current"]["temperature_2m"]


def popis_pocasia(kod):
    """Prelozi cislo stavu pocasia na slovensky text (neznamy kod -> 'neznamy stav')."""
    return POPISY_POCASIA.get(kod, "neznamy stav")


def emoji_pocasia(kod):
    """Vrati emoji k stavu pocasia (neznamy kod -> otaznik)."""
    return EMOJI_POCASIA.get(kod, "❓")


def nazov_dna(index, datum_str):
    """Pomenuje den: 0 -> 'Dnes', 1 -> 'Zajtra', inak nazov dna + datum (napr. 'Streda 11.6.').
    datum_str je v tvare 'RRRR-MM-DD' (z predpovede)."""
    if index == 0:
        return "Dnes"
    if index == 1:
        return "Zajtra"
    den = datetime.strptime(datum_str, "%Y-%m-%d")
    return f"{DNI_V_TYZDNI[den.weekday()]} {den.day}.{den.month}."


def predpoved_z_dat(data):
    """Z odpovede zostavi zoznam dni (nazov, emoji, stav, max, min teplota)."""
    d = data["daily"]
    dni = []
    for i, datum in enumerate(d["time"]):
        kod = d["weather_code"][i]
        dni.append({
            "nazov": nazov_dna(i, datum),
            "emoji": emoji_pocasia(kod),
            "stav": popis_pocasia(kod),
            "max": d["temperature_2m_max"][i],
            "min": d["temperature_2m_min"][i],
        })
    return dni


# --- Obsluha ---

def main():
    nazov = input("Zadaj mesto: ").strip()
    if not nazov:
        print("Nezadal si ziadne mesto.")
        return
    try:
        mesto = najdi_mesto(nazov)                 # 1) nazov -> suradnice
        if mesto is None:
            print(f"Mesto '{nazov}' som nenasiel, skus iny nazov.")
            return
        data = stiahni_pocasie(mesto["latitude"], mesto["longitude"])  # 2) suradnice -> pocasie
    except requests.exceptions.RequestException:
        print("Nepodarilo sa spojit so sluzbou pocasia. Skontroluj internet a skus znova.")
        return

    current = data["current"]
    krajina = mesto.get("country", "")
    print(f"\nPocasie v meste {mesto['name']} ({krajina}):")
    print(f"  Teplota:  {current['temperature_2m']} °C (pocitovo {current['apparent_temperature']} °C)")
    print(f"  Stav:     {popis_pocasia(current['weather_code'])}")


if __name__ == "__main__":
    main()
