# pocasie.py - Projekt 6, Etapa 2: zadaj mesto -> appka zisti suradnice a pocasie.
# Dve volania API za sebou:
#   1) geocoding (nazov mesta -> suradnice)   2) forecast (suradnice -> teplota)
# Open-Meteo: https://open-meteo.com  (netreba API kluc)

import requests


# --- Praca s API ---

def najdi_mesto(nazov):
    """Cez geocoding API zisti udaje o meste. Vrati slovnik prveho vysledku, alebo None."""
    odpoved = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": nazov, "count": 1, "language": "sk", "format": "json"},
        timeout=10,
    )
    odpoved.raise_for_status()
    vysledky = odpoved.json().get("results")  # ak nic nenajde, kluc "results" chyba
    if not vysledky:
        return None
    return vysledky[0]


def stiahni_pocasie(lat, lon):
    """Posle GET poziadavku na Open-Meteo a vrati odpoved ako Python slovnik (z JSON)."""
    odpoved = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": lat, "longitude": lon, "current": "temperature_2m"},
        timeout=10,
    )
    odpoved.raise_for_status()
    return odpoved.json()


# --- Cista logika (da sa testovat bez internetu) ---

def teplota_z_dat(data):
    """Z odpovede (slovnik) vytiahne aktualnu teplotu."""
    return data["current"]["temperature_2m"]


# --- Obsluha ---

def main():
    nazov = input("Zadaj mesto: ").strip()
    if not nazov:
        print("Nezadal si ziadne mesto.")
        return
    mesto = najdi_mesto(nazov)          # 1) nazov -> suradnice
    if mesto is None:
        print(f"Mesto '{nazov}' som nenasiel, skus iny nazov.")
        return
    data = stiahni_pocasie(mesto["latitude"], mesto["longitude"])  # 2) suradnice -> pocasie
    teplota = teplota_z_dat(data)
    krajina = mesto.get("country", "")
    print(f"Aktualna teplota v meste {mesto['name']} ({krajina}): {teplota} °C")


if __name__ == "__main__":
    main()
