# vydavky.py - Spravca vydavkov (Projekt 3), Etapa A: MVP s databazou (SQLite).
# Jeden vydavok = suma + kategoria + datum + poznamka. Data sa ukladaju do suboru vydavky.db.
# SQLite je databaza vstavana priamo v Pythone - netreba nic instalovat.

import os
import sqlite3
from datetime import date

from dotenv import load_dotenv

# Nacitanie nastaveni zo suboru .env (mimo kodu). Ak .env chyba, pouziju sa zalozne hodnoty.
load_dotenv()
SUBOR_DB = os.getenv("DB_SUBOR", "vydavky.db")  # nazov suboru s databazou
MENA = os.getenv("MENA", "EUR")                 # mena pre vypis (napr. EUR, CZK)


# --- Praca s databazou ---

def pripoj():
    """Otvori (alebo vytvori) databazovy subor a vrati spojenie."""
    return sqlite3.connect(SUBOR_DB)


def vytvor_tabulku(conn):
    """Vytvori tabulku 'vydavky', ak este neexistuje.
    Stlpce: id (samo sa cisluje), suma, kategoria, datum, poznamka."""
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS vydavky (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            suma REAL NOT NULL,
            kategoria TEXT NOT NULL,
            datum TEXT NOT NULL,
            poznamka TEXT
        )
        """
    )
    conn.commit()


def pridaj_vydavok(conn, suma, kategoria, datum, poznamka):
    """Prida jeden vydavok (jeden riadok) do tabulky. SQL prikaz: INSERT."""
    conn.execute(
        "INSERT INTO vydavky (suma, kategoria, datum, poznamka) VALUES (?, ?, ?, ?)",
        (suma, kategoria, datum, poznamka),
    )
    conn.commit()


def vsetky_vydavky(conn):
    """Vrati vsetky vydavky ako zoznam riadkov. SQL prikaz: SELECT."""
    kurzor = conn.execute(
        "SELECT id, suma, kategoria, datum, poznamka FROM vydavky ORDER BY datum"
    )
    return kurzor.fetchall()


# --- Pomocna funkcia ---

def parsuj_sumu(text):
    """Prevedie text na cislo (akceptuje ciarku); vrati None, ak to nie je platne cislo."""
    text = text.strip().replace(",", ".")
    try:
        return float(text)
    except ValueError:
        return None


# --- Obsluha (menu / input / vypis) ---

def pridaj(conn):
    suma = parsuj_sumu(input("Suma: "))
    if suma is None:
        print("To nie je platna suma, skus znova.")
        return
    kategoria = input("Kategoria (napr. jedlo, doprava): ").strip() or "ine"
    zadany_datum = input(f"Datum (Enter = dnes {date.today()}): ").strip()
    datum = zadany_datum if zadany_datum else str(date.today())
    poznamka = input("Poznamka (nepovinne): ").strip()
    pridaj_vydavok(conn, suma, kategoria, datum, poznamka)
    print(f"Pridane: {suma} - {kategoria} ({datum})")


def zobraz(conn):
    riadky = vsetky_vydavky(conn)
    if not riadky:
        print("Zatial ziadne vydavky.")
        return
    print("--- Tvoje vydavky ---")
    for r in riadky:
        id_, suma, kategoria, datum, poznamka = r
        pozn = f" - {poznamka}" if poznamka else ""
        print(f"#{id_}  {datum}  {suma:>8.2f} {MENA}  [{kategoria}]{pozn}")


def main():
    conn = pripoj()
    vytvor_tabulku(conn)
    while True:
        print("\n=== SPRAVCA VYDAVKOV ===")
        print("1) Pridat vydavok")
        print("2) Zobrazit vsetky")
        print("3) Koniec")
        volba = input("Vyber (1-3): ").strip()
        if volba == "1":
            pridaj(conn)
        elif volba == "2":
            zobraz(conn)
        elif volba == "3":
            print("Dovidenia!")
            break
        else:
            print("Neplatna volba, skus 1-3.")
    conn.close()


if __name__ == "__main__":
    main()
