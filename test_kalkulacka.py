# test_kalkulacka.py - automaticky "robot", ktory otestuje vsetky funkcie kalkulacky.
# Spustenie:  python test_kalkulacka.py
# Testujeme "cistu logiku" z kalkulacka.py (ziadny input ani vypis menu).

import kalkulacka as k

vysledky = []


def skontroluj(nazov, podmienka):
    """Zapise vysledok jedneho testu a vypise PASS/FAIL."""
    vysledky.append(bool(podmienka))
    print(("[PASS] " if podmienka else "[FAIL] ") + nazov)


# --- Test 1: pridavanie cisel ---
cisla = []
k.pridaj_cislo(cisla, 2)
k.pridaj_cislo(cisla, 7)
skontroluj("pridanie prida dve cisla", cisla == [2, 7])

# --- Test 2: scitanie ---
skontroluj("scitanie 2 + 7 = 9", k.scitaj([2, 7]) == 9)
skontroluj("scitanie prazdneho zoznamu = 0", k.scitaj([]) == 0)

# --- Test 3: odcitanie ---
skontroluj("odcitanie 8 - 6 = 2", k.odcitaj([8, 6]) == 2)
skontroluj("odcitanie 10 - 3 - 2 = 5", k.odcitaj([10, 3, 2]) == 5)

# --- Test 4: nasobenie ---
skontroluj("nasobenie 5 * 8 = 40", k.nasob([5, 8]) == 40)
skontroluj("nasobenie prazdneho zoznamu = 0", k.nasob([]) == 0)

# --- Test 5: delenie ---
skontroluj("delenie 8 / 2 = 4", k.vydel([8, 2]) == 4)
skontroluj("delenie nulou vrati None (chyba)", k.vydel([8, 0]) is None)

# --- Test 6: pomocne funkcie ---
skontroluj("parsuj_cislo('5') = 5", k.parsuj_cislo("5") == 5)
skontroluj("parsuj_cislo('3,5') = 3.5 (ciarka)", k.parsuj_cislo("3,5") == 3.5)
skontroluj("parsuj_cislo('abc') = None", k.parsuj_cislo("abc") is None)
skontroluj("uprav_vystup(9.0) = 9 (bez .0)", k.uprav_vystup(9.0) == 9)

# --- Test 7: retazenie (vysledok ako novy zaklad) ---
# 2 + 7 = 9, potom 9 * 2 = 18
medzi = k.scitaj([2, 7])
skontroluj("retazenie: (2+7) potom *2 = 18", k.nasob([medzi, 2]) == 18)


# --- Suhrn ---
print("-" * 40)
preslo = sum(vysledky)
spolu = len(vysledky)
if preslo == spolu:
    print(f"VYSLEDOK: vsetkych {spolu} testov PRESLO.")
else:
    print(f"VYSLEDOK: {preslo}/{spolu} preslo, {spolu - preslo} ZLYHALO.")
