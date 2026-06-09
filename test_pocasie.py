# test_pocasie.py - automaticke testy pre cistu logiku z pocasie.py.
# Spustenie:  python test_pocasie.py
# Testujeme BEZ internetu - funkciam podstrcime vymyslene data (ake vracia API).

import pocasie as p

vysledky = []


def skontroluj(nazov, podmienka):
    """Zapise vysledok jedneho testu a vypise PASS/FAIL."""
    vysledky.append(bool(podmienka))
    print(("[PASS] " if podmienka else "[FAIL] ") + nazov)


# --- Test 1: popis_pocasia (kod -> text) ---
skontroluj("popis 0 = jasno", p.popis_pocasia(0) == "jasno")
skontroluj("popis 61 = slaby dazd", p.popis_pocasia(61) == "slaby dazd")
skontroluj("popis neznameho kodu = neznamy stav", p.popis_pocasia(999) == "neznamy stav")

# --- Test 2: emoji_pocasia (kod -> emoji) ---
skontroluj("emoji 0 = slnko", p.emoji_pocasia(0) == "☀️")
skontroluj("emoji 2 = polojasno", p.emoji_pocasia(2) == "⛅")
skontroluj("emoji neznameho kodu = otaznik", p.emoji_pocasia(999) == "❓")

# --- Test 3: nazov_dna (index + datum -> nazov) ---
skontroluj("index 0 = Dnes", p.nazov_dna(0, "2026-06-09") == "Dnes")
skontroluj("index 1 = Zajtra", p.nazov_dna(1, "2026-06-10") == "Zajtra")
skontroluj("index 2 obsahuje datum 11.6.", p.nazov_dna(2, "2026-06-11").endswith("11.6."))

# --- Test 4: predpoved_z_dat (vymyslene data -> zoznam dni) ---
falosne_data = {
    "daily": {
        "time": ["2026-06-09", "2026-06-10", "2026-06-11"],
        "weather_code": [0, 61, 2],
        "temperature_2m_max": [28.5, 20.0, 24.0],
        "temperature_2m_min": [17.0, 15.0, 16.0],
    }
}
dni = p.predpoved_z_dat(falosne_data)
skontroluj("predpoved ma 3 dni", len(dni) == 3)
skontroluj("prvy den je Dnes", dni[0]["nazov"] == "Dnes")
skontroluj("prvy den max = 28.5", dni[0]["max"] == 28.5)
skontroluj("prvy den stav = jasno", dni[0]["stav"] == "jasno")
skontroluj("prvy den emoji = slnko", dni[0]["emoji"] == "☀️")


# --- Suhrn ---
print("-" * 40)
preslo = sum(vysledky)
spolu = len(vysledky)
if preslo == spolu:
    print(f"VYSLEDOK: vsetkych {spolu} testov PRESLO.")
else:
    print(f"VYSLEDOK: {preslo}/{spolu} preslo, {spolu - preslo} ZLYHALO.")
