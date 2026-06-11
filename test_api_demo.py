# test_api_demo.py - testy pre API endpoint /api/vypocet.
# Spustenie:  python test_api_demo.py
# Pouzivame Flask test client - posiela poziadavky BEZ spustenia servera.

import api_demo

vysledky = []
cli = api_demo.app.test_client()


def skontroluj(nazov, podmienka):
    vysledky.append(bool(podmienka))
    print(("[PASS] " if podmienka else "[FAIL] ") + nazov)


def vysledok(a, b, op):
    """Pomocnik: zavola API a vrati (stav, JSON)."""
    r = cli.get(f"/api/vypocet?a={a}&b={b}&op={op}")
    return r.status_code, r.get_json()


# --- Operacie ---
st, d = vysledok(2, 3, "scitaj")
skontroluj("2 + 3 = 5", st == 200 and d["vysledok"] == 5)
st, d = vysledok(8, 2, "odcitaj")
skontroluj("8 - 2 = 6", st == 200 and d["vysledok"] == 6)
st, d = vysledok(5, 8, "nasob")
skontroluj("5 * 8 = 40", st == 200 and d["vysledok"] == 40)
st, d = vysledok(8, 2, "delit")
skontroluj("8 / 2 = 4", st == 200 and d["vysledok"] == 4)

# --- Osetrenie chyb ---
st, d = vysledok(8, 0, "delit")
skontroluj("delenie nulou -> stav 400 + chyba", st == 400 and "chyba" in d)
st, d = vysledok(2, "abc", "scitaj")
skontroluj("neplatne cislo -> stav 400 + chyba", st == 400 and "chyba" in d)
st, d = vysledok(2, 3, "mocnina")
skontroluj("neznama operacia -> stav 400 + chyba", st == 400 and "chyba" in d)


# --- Suhrn ---
print("-" * 40)
preslo = sum(vysledky)
spolu = len(vysledky)
if preslo == spolu:
    print(f"VYSLEDOK: vsetkych {spolu} testov PRESLO.")
else:
    print(f"VYSLEDOK: {preslo}/{spolu} preslo, {spolu - preslo} ZLYHALO.")
