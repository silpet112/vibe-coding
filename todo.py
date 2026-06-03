# todo.py - jednoduchy Spravca uloh (MVP)
# Funkcie: pridat ulohu, zobrazit zoznam, oznacit hotovu, ulozit do suboru.

import json
import os

SUBOR = "ulohy.json"  # sem sa ukladaju ulohy, aby ostali aj po zatvoreni

# Farby pre terminal (ANSI). Prioritne ulohy budu bledo zelene.
ZELENA = "\033[92m"
RESET = "\033[0m"


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


# --- Cista logika (testovatelna: ziadny input, print ani subor) ---

def pridaj_ulohu(ulohy, text):
    """Prida novu ulohu do zoznamu."""
    ulohy.append({"text": text, "hotovo": False, "priorita": False})


def oznac_ako_hotovu(ulohy, index):
    """Oznaci ulohu na danom indexe ako hotovu."""
    ulohy[index]["hotovo"] = True


def zmaz_ulohu(ulohy, index):
    """Odstrani ulohu na danom indexe."""
    ulohy.pop(index)


def prepni_prioritu(ulohy, index):
    """Prepne prioritu ulohy a vrati jej novy stav (True/False)."""
    ulohy[index]["priorita"] = not ulohy[index].get("priorita", False)
    return ulohy[index]["priorita"]


# --- Obsluha (input / vypis / ukladanie) ---


def pridaj(ulohy):
    text = input("Nazov ulohy: ").strip()
    if text:
        pridaj_ulohu(ulohy, text)
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
        text = u["text"]
        if u.get("priorita", False):
            text = ZELENA + "* " + text + RESET  # prioritna uloha = bledo zeleny text
        print(f"{i}. {znacka} {text}")


def oznac_hotovu(ulohy):
    zobraz(ulohy)
    if not ulohy:
        return
    volba = input("Cislo ulohy na oznacenie ako hotovej: ").strip()
    if volba.isdigit() and 1 <= int(volba) <= len(ulohy):
        oznac_ako_hotovu(ulohy, int(volba) - 1)
        uloz_ulohy(ulohy)
        print("Oznacene ako hotove.")
    else:
        print("Neplatne cislo.")


def zmazat(ulohy):
    zobraz(ulohy)
    if not ulohy:
        return
    volba = input("Cislo ulohy na zmazanie: ").strip()
    if volba.isdigit() and 1 <= int(volba) <= len(ulohy):
        index = int(volba) - 1
        nazov = ulohy[index]["text"]
        # Potvrdenie pred zmazanim (bezpecnostna otazka)
        potvrd = input(f"Naozaj zmazat '{nazov}'? (a/n): ").strip().lower()
        if potvrd in ("a", "ano", "y", "yes"):
            zmaz_ulohu(ulohy, index)
            uloz_ulohy(ulohy)
            print("Zmazane.")
        else:
            print("Zrusene - nic som nezmazal.")
    else:
        print("Neplatne cislo.")


def nastav_prioritu(ulohy):
    zobraz(ulohy)
    if not ulohy:
        return
    volba = input("Cislo ulohy pre prioritu (prepnut): ").strip()
    if volba.isdigit() and 1 <= int(volba) <= len(ulohy):
        index = int(volba) - 1
        je_prioritna = prepni_prioritu(ulohy, index)
        uloz_ulohy(ulohy)
        print("Uloha je teraz prioritna." if je_prioritna else "Priorita zrusena.")
    else:
        print("Neplatne cislo.")


def main():
    os.system("")  # zapne farebny (ANSI) vystup v termini na Windows
    ulohy = nacitaj_ulohy()
    while True:
        print("\n=== SPRAVCA ULOH ===")
        print("1) Pridat ulohu")
        print("2) Zobrazit zoznam")
        print("3) Oznacit ulohu ako hotovu")
        print("4) Zmazat ulohu")
        print("5) Nastavit prioritu (zvyrazni zelenou)")
        print("6) Koniec")
        volba = input("Vyber (1-6): ").strip()
        if volba == "1":
            pridaj(ulohy)
        elif volba == "2":
            zobraz(ulohy)
        elif volba == "3":
            oznac_hotovu(ulohy)
        elif volba == "4":
            zmazat(ulohy)
        elif volba == "5":
            nastav_prioritu(ulohy)
        elif volba == "6":
            print("Dovidenia!")
            break
        else:
            print("Neplatna volba, skus 1-6.")


if __name__ == "__main__":
    main()
