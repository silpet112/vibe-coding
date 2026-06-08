# pocasie.py - Projekt 6, Etapa 3: krajsi vypis (pocitova teplota + slovny popis) + osetrenie chyb.
# Dve volania API: 1) geocoding (mesto -> suradnice)  2) forecast (suradnice -> pocasie).
# Open-Meteo: https://open-meteo.com  (netreba API kluc)

import requests

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
    """Vrati aktualne pocasie (teplota, pocitova teplota, kod stavu) ako slovnik."""
    odpoved = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,apparent_temperature,weather_code",
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
