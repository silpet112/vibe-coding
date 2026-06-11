# test_prihlasenie.py - testy prihlasenia a ochrany stranky.
# Spustenie:  python test_prihlasenie.py
# Pouzivame Flask test client (kazdy test ma vlastneho klienta = cistu session).

import prihlasenie

vysledky = []


def skontroluj(nazov, podmienka):
    vysledky.append(bool(podmienka))
    print(("[PASS] " if podmienka else "[FAIL] ") + nazov)


def novy_klient():
    return prihlasenie.app.test_client()


# --- Test 1: neprihlaseny sa nedostane na /tajne (presmerovanie 302) ---
c = novy_klient()
skontroluj("neprihlaseny -> /tajne presmeruje (302)", c.get("/tajne").status_code == 302)

# --- Test 2: zle heslo neprihlasi ---
c = novy_klient()
c.post("/prihlas", data={"meno": "admin", "heslo": "zle"})
skontroluj("zle heslo -> /tajne stale 302", c.get("/tajne").status_code == 302)

# --- Test 3: neznamy pouzivatel sa neprihlasi ---
c = novy_klient()
c.post("/prihlas", data={"meno": "nikto", "heslo": "tajne123"})
skontroluj("neznamy pouzivatel -> /tajne 302", c.get("/tajne").status_code == 302)

# --- Test 4: spravne heslo prihlasi a pusti na /tajne ---
c = novy_klient()
c.post("/prihlas", data={"meno": "admin", "heslo": "tajne123"})
r = c.get("/tajne")
skontroluj("spravne heslo -> /tajne pristupne (200)", r.status_code == 200)
skontroluj("tajna stranka obsahuje meno admin", "admin" in r.get_data(as_text=True))

# --- Test 5: po odhlaseni zase chranene ---
c = novy_klient()
c.post("/prihlas", data={"meno": "admin", "heslo": "tajne123"})
skontroluj("po prihlaseni /tajne 200", c.get("/tajne").status_code == 200)
c.get("/odhlas")
skontroluj("po odhlaseni /tajne zase 302", c.get("/tajne").status_code == 302)


# --- Suhrn ---
print("-" * 40)
preslo = sum(vysledky)
spolu = len(vysledky)
if preslo == spolu:
    print(f"VYSLEDOK: vsetkych {spolu} testov PRESLO.")
else:
    print(f"VYSLEDOK: {preslo}/{spolu} preslo, {spolu - preslo} ZLYHALO.")
