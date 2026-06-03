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


def main():
    conn = databaza.pripoj()
    databaza.vytvor_tabulku(conn)
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
