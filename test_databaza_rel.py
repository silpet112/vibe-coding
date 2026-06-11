# test_databaza_rel.py - testy relacnej datovej vrstvy (databaza_rel.py).
# Spustenie:  python test_databaza_rel.py
# Vsetko bezi na DB v PAMATI (':memory:') - nic sa neuklada.

import sqlite3

import databaza_rel as db

vysledky = []


def skontroluj(nazov, podmienka):
    vysledky.append(bool(podmienka))
    print(("[PASS] " if podmienka else "[FAIL] ") + nazov)


def nova_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    db.vytvor_tabulky(conn)
    return conn


# --- Test 1: kategorie sa nezduplikuju, dostavaju spravne id ---
conn = nova_db()
id1 = db.id_kategorie(conn, "jedlo")
id2 = db.id_kategorie(conn, "jedlo")          # to iste meno
skontroluj("rovnaka kategoria -> rovnake id", id1 == id2)
skontroluj("kategoria je v tabulke len raz", len(db.vsetky_kategorie(conn)) == 1)
id3 = db.id_kategorie(conn, "doprava")
skontroluj("nova kategoria -> ine id", id3 != id1)

# --- Test 2: pridanie vydavkov + JOIN vrati nazov kategorie ---
conn = nova_db()
db.pridaj_vydavok(conn, 4.5, "jedlo", "2026-06-01", "obed")
db.pridaj_vydavok(conn, 6.0, "jedlo", "2026-06-02", "")
db.pridaj_vydavok(conn, 12.0, "doprava", "2026-06-03", "")
riadky = db.vsetky_vydavky(conn)
skontroluj("pridane 3 vydavky", len(riadky) == 3)
skontroluj("JOIN vrati nazov kategorie (prvy = jedlo)", riadky[0][2] == "jedlo")
skontroluj("kategorie su len 2 (jedlo 2x sa nezdvojila)", len(db.vsetky_kategorie(conn)) == 2)

# --- Test 3: sucet podla kategorie (JOIN + GROUP BY) ---
sucty = dict(db.sucet_podla_kategorie(conn))
skontroluj("jedlo spolu = 10.5", sucty["jedlo"] == 10.5)
skontroluj("doprava spolu = 12.0", sucty["doprava"] == 12.0)


# --- Suhrn ---
print("-" * 40)
preslo = sum(vysledky)
spolu = len(vysledky)
if preslo == spolu:
    print(f"VYSLEDOK: vsetkych {spolu} testov PRESLO.")
else:
    print(f"VYSLEDOK: {preslo}/{spolu} preslo, {spolu - preslo} ZLYHALO.")
