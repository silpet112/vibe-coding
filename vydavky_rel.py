# vydavky_rel.py - Projekt 8, Etapa 3: terminalove menu nad RELACNOU databazou (databaza_rel.py).
# Kategoria je vlastna tabulka; vypis ide cez JOIN. Znova pouziva logika.parsuj_sumu z Projektu 3.
# Spustenie:  python vydavky_rel.py

from datetime import date

import databaza_rel as db
import logika  # znova pouzita funkcia parsuj_sumu


def pridaj(conn):
    suma = logika.parsuj_sumu(input("Suma: "))
    if suma is None:
        print("To nie je platna suma, skus znova.")
        return
    kategoria = input("Kategoria (napr. jedlo, doprava): ").strip() or "ine"
    zadany_datum = input(f"Datum (Enter = dnes {date.today()}): ").strip()
    datum = zadany_datum if zadany_datum else str(date.today())
    poznamka = input("Poznamka (nepovinne): ").strip()
    db.pridaj_vydavok(conn, suma, kategoria, datum, poznamka)
    print(f"Pridane: {suma} [{kategoria}] ({datum})")


def zobraz(conn):
    riadky = db.vsetky_vydavky(conn)  # cez JOIN -> aj nazov kategorie
    if not riadky:
        print("Zatial ziadne vydavky.")
        return
    print("--- Tvoje vydavky ---")
    for id_, suma, kategoria, datum, poznamka in riadky:
        pozn = f" - {poznamka}" if poznamka else ""
        print(f"#{id_}  {datum}  {suma:>8.2f}  [{kategoria}]{pozn}")


def prehlad(conn):
    riadky = db.sucet_podla_kategorie(conn)  # JOIN + GROUP BY
    if not riadky:
        print("Zatial ziadne vydavky.")
        return
    print("--- Sucet podla kategorie ---")
    for kategoria, sucet in riadky:
        print(f"{kategoria:<15} {sucet:>8.2f}")


def zobraz_kategorie(conn):
    print("--- Kategorie (vlastna tabulka) ---")
    for kid, nazov in db.vsetky_kategorie(conn):
        print(f"{kid}. {nazov}")


def main():
    conn = db.pripoj()
    db.vytvor_tabulky(conn)
    while True:
        print("\n=== VYDAVKY (relacna verzia) ===")
        print("1) Pridat vydavok")
        print("2) Zobrazit vsetky")
        print("3) Prehlad podla kategorie")
        print("4) Zoznam kategorii")
        print("5) Koniec")
        volba = input("Vyber (1-5): ").strip()
        if volba == "1":
            pridaj(conn)
        elif volba == "2":
            zobraz(conn)
        elif volba == "3":
            prehlad(conn)
        elif volba == "4":
            zobraz_kategorie(conn)
        elif volba == "5":
            print("Dovidenia!")
            conn.close()
            break
        else:
            print("Neplatna volba, skus 1-5.")


if __name__ == "__main__":
    main()
