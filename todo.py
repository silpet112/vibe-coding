# todo.py - jednoduchy Spravca uloh (MVP)
# Funkcie: pridat ulohu, zobrazit zoznam, oznacit hotovu, ulozit do suboru.

import json
import os

SUBOR = "ulohy.json"  # sem sa ukladaju ulohy, aby ostali aj po zatvoreni


def nacitaj_ulohy():
    """Nacita ulohy zo suboru. Ak subor neexistuje alebo je poskodeny,
    vrati prazdny zoznam (poistka, aby program nespadol)."""
    if os.path.exists(SUBOR):
        try:
            with open(SUBOR, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Pozor: subor s ulohami sa neda precitat, zacinam s prazdnym zoznamom.")
            return []
    return []


def uloz_ulohy(ulohy):
    """Ulozi ulohy do suboru."""
    with open(SUBOR, "w", encoding="utf-8") as f:
        json.dump(ulohy, f, ensure_ascii=False, indent=2)


def pridaj(ulohy):
    text = input("Nazov ulohy: ").strip()
    if text:
        ulohy.append({"text": text, "hotovo": False})
        uloz_ulohy(ulohy)
        print(f"Pridane: {text}")
    else:
        print("Prazdny nazov - nic som nepridal.")


def zobraz(ulohy):
    if not ulohy:
        print("Zoznam je prazdny.")
        return
    print("--- Tvoje ulohy ---")
    for i, u in enumerate(ulohy, start=1):
        znacka = "[x]" if u["hotovo"] else "[ ]"
        print(f"{i}. {znacka} {u['text']}")


def oznac_hotovu(ulohy):
    zobraz(ulohy)
    if not ulohy:
        return
    volba = input("Cislo ulohy na oznacenie ako hotovej: ").strip()
    if volba.isdigit() and 1 <= int(volba) <= len(ulohy):
        ulohy[int(volba) - 1]["hotovo"] = True
        uloz_ulohy(ulohy)
        print("Oznacene ako hotove.")
    else:
        print("Neplatne cislo.")


def main():
    ulohy = nacitaj_ulohy()
    while True:
        print("\n=== SPRAVCA ULOH ===")
        print("1) Pridat ulohu")
        print("2) Zobrazit zoznam")
        print("3) Oznacit ulohu ako hotovu")
        print("4) Koniec")
        volba = input("Vyber (1-4): ").strip()
        if volba == "1":
            pridaj(ulohy)
        elif volba == "2":
            zobraz(ulohy)
        elif volba == "3":
            oznac_hotovu(ulohy)
        elif volba == "4":
            print("Dovidenia!")
            break
        else:
            print("Neplatna volba, skus 1-4.")


if __name__ == "__main__":
    main()
