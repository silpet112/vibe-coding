# kalkulacka.py - jednoducha kalkulacka (scitanie a odcitanie)
# Menu: pridat cislo, scitat, odcitat, koniec.
# Priklad: pridas 2 a 7 -> scitat = 9 ;  pridas 8 a 6 -> odcitat = 2

# --- Cista logika (da sa lahko testovat) ---

def pridaj_cislo(cisla, hodnota):
    """Prida cislo do zoznamu zadanych cisel."""
    cisla.append(hodnota)


def scitaj(cisla):
    """Scita vsetky zadane cisla. Napr. [2, 7] -> 9."""
    return sum(cisla)


def odcitaj(cisla):
    """Od prveho cisla postupne odcita ostatne. Napr. [8, 6] -> 2."""
    if not cisla:
        return 0
    vysledok = cisla[0]
    for c in cisla[1:]:
        vysledok -= c
    return vysledok


def nasob(cisla):
    """Vynasobi vsetky cisla. Napr. [5, 8] -> 40."""
    if not cisla:
        return 0
    vysledok = 1
    for c in cisla:
        vysledok *= c
    return vysledok


def vydel(cisla):
    """Prve cislo postupne vydeli ostatnymi. Napr. [8, 2] -> 4.
    Pri deleni nulou vrati None (chyba)."""
    if not cisla:
        return 0
    vysledok = cisla[0]
    for c in cisla[1:]:
        if c == 0:
            return None
        vysledok /= c
    return vysledok


# --- Pomocne funkcie ---

def parsuj_cislo(text):
    """Prevedie text na cislo (int alebo float); vrati None, ak to nie je cislo."""
    text = text.strip().replace(",", ".")  # akceptuj ciarku aj bodku
    try:
        return float(text) if "." in text else int(text)
    except ValueError:
        return None


def uprav_vystup(cislo):
    """Pekny vystup: cele cislo bez '.0' (napr. 9.0 -> 9)."""
    if isinstance(cislo, float) and cislo.is_integer():
        return int(cislo)
    return cislo


# --- Obsluha (menu) ---

def main():
    cisla = []
    while True:
        print("\n=== KALKULACKA ===")
        if cisla:
            print("Zadane cisla:", cisla)
        print("1) Pridat cislo")
        print("2) Scitat")
        print("3) Odcitat")
        print("4) Nasobit")
        print("5) Delit")
        print("6) Koniec")
        volba = input("Vyber (1-6): ").strip()
        if volba == "1":
            hodnota = parsuj_cislo(input("Zadaj cislo: "))
            if hodnota is None:
                print("To nie je platne cislo, skus znova.")
            else:
                pridaj_cislo(cisla, hodnota)
                print(f"Pridane: {uprav_vystup(hodnota)}")
        elif volba == "2":
            vysledok = scitaj(cisla)
            print(f"Sucet = {uprav_vystup(vysledok)}")
            cisla = [vysledok]  # vysledok = novy zaklad pre dalsiu operaciu
        elif volba == "3":
            vysledok = odcitaj(cisla)
            print(f"Rozdiel = {uprav_vystup(vysledok)}")
            cisla = [vysledok]
        elif volba == "4":
            vysledok = nasob(cisla)
            print(f"Sucin = {uprav_vystup(vysledok)}")
            cisla = [vysledok]
        elif volba == "5":
            vysledok = vydel(cisla)
            if vysledok is None:
                print("Chyba: delenie nulou nie je mozne.")
            else:
                print(f"Podiel = {uprav_vystup(vysledok)}")
                cisla = [vysledok]
        elif volba == "6":
            print("Dovidenia!")
            break
        else:
            print("Neplatna volba, skus 1-6.")


if __name__ == "__main__":
    main()
