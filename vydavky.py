# vydavky.py - Spravca vydavkov (Projekt 3). Vrstva OBSLUHA: menu, input, vypis.
# Architektura (vrstvy):
#   konfig.py   - nastavenia (.env)
#   databaza.py - praca so SQLite (SQL)
#   logika.py   - ciste vypocty
#   vydavky.py  - toto: menu a komunikacia s pouzivatelom
# Spustenie:  python vydavky.py

from datetime import date

import konfig
import databaza
import logika


def pridaj(conn):
    suma = logika.parsuj_sumu(input("Suma: "))
    if suma is None:
        print("To nie je platna suma, skus znova.")
        return
    kategoria = input("Kategoria (napr. jedlo, doprava): ").strip() or "ine"
    zadany_datum = input(f"Datum (Enter = dnes {date.today()}): ").strip()
    datum = zadany_datum if zadany_datum else str(date.today())
    poznamka = input("Poznamka (nepovinne): ").strip()
    databaza.pridaj_vydavok(conn, suma, kategoria, datum, poznamka)
    print(f"Pridane: {suma} - {kategoria} ({datum})")


def zobraz(conn):
    riadky = databaza.vsetky_vydavky(conn)
    if not riadky:
        print("Zatial ziadne vydavky.")
        return
    print("--- Tvoje vydavky ---")
    for r in riadky:
        id_, suma, kategoria, datum, poznamka = r
        pozn = f" - {poznamka}" if poznamka else ""
        print(f"#{id_}  {datum}  {suma:>8.2f} {konfig.MENA}  [{kategoria}]{pozn}")


def prehlad_spolu(conn):
    spolu = databaza.sucet_vsetkych(conn)
    print(f"Spolu si minul: {spolu:.2f} {konfig.MENA}")


def prehlad_kategorie(conn):
    riadky = databaza.sucet_podla_kategorie(conn)
    if not riadky:
        print("Zatial ziadne vydavky.")
        return
    print("--- Vydavky podla kategorie ---")
    for kategoria, sucet in riadky:
        print(f"{kategoria:<15} {sucet:>8.2f} {konfig.MENA}")


def prehlad_mesiac(conn):
    zadanie = input(f"Mesiac (RRRR-MM, Enter = tento {date.today():%Y-%m}): ").strip()
    rok_mesiac = zadanie if zadanie else f"{date.today():%Y-%m}"
    spolu = databaza.sucet_za_mesiac(conn, rok_mesiac)
    print(f"Vydavky za {rok_mesiac}: {spolu:.2f} {konfig.MENA}")


def main():
    conn = databaza.pripoj()
    databaza.vytvor_tabulku(conn)
    while True:
        print("\n=== SPRAVCA VYDAVKOV ===")
        print("1) Pridat vydavok")
        print("2) Zobrazit vsetky")
        print("3) Prehlad: spolu")
        print("4) Prehlad: podla kategorie")
        print("5) Prehlad: za mesiac")
        print("6) Koniec")
        volba = input("Vyber (1-6): ").strip()
        if volba == "1":
            pridaj(conn)
        elif volba == "2":
            zobraz(conn)
        elif volba == "3":
            prehlad_spolu(conn)
        elif volba == "4":
            prehlad_kategorie(conn)
        elif volba == "5":
            prehlad_mesiac(conn)
        elif volba == "6":
            print("Dovidenia!")
            break
        else:
            print("Neplatna volba, skus 1-6.")
    conn.close()


if __name__ == "__main__":
    main()
