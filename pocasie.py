# pocasie.py - Projekt 6, Etapa 1: prve volanie API (Open-Meteo, zadarmo, bez kluca).
# Stiahne aktualnu teplotu pre pevne suradnice (Bratislava) a vypise ju.
# Open-Meteo: https://open-meteo.com  (netreba API kluc)

import requests

# Suradnice Bratislavy (sirka/dlzka). V Etape 2 ich zistime z nazvu mesta cez geocoding API.
LATITUDE = 48.15
LONGITUDE = 17.11


# --- Praca s API ---

def stiahni_pocasie(lat, lon):
    """Posle GET poziadavku na Open-Meteo a vrati odpoved ako Python slovnik (z JSON)."""
    odpoved = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": lat, "longitude": lon, "current": "temperature_2m"},
        timeout=10,
    )
    odpoved.raise_for_status()  # ak server nevrati 200 (OK), vyhodi chybu
    return odpoved.json()       # premeni JSON odpoved na Python slovnik


# --- Cista logika (da sa testovat bez internetu) ---

def teplota_z_dat(data):
    """Z odpovede (slovnik) vytiahne aktualnu teplotu."""
    return data["current"]["temperature_2m"]


# --- Obsluha ---

def main():
    data = stiahni_pocasie(LATITUDE, LONGITUDE)
    teplota = teplota_z_dat(data)
    print(f"Aktualna teplota v Bratislave: {teplota} °C")


if __name__ == "__main__":
    main()
