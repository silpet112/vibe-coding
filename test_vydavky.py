# test_vydavky.py - automaticky "robot", ktory otestuje Spravcu vydavkov.
# Spustenie:  python test_vydavky.py
# Testuje vrstvy logika.py a databaza.py. Databaza bezi v PAMATI (':memory:'),
# takze sa NEDOTKNE tvojich realnych dat (vydavky.db).

import logika
import databaza

vysledky = []


def skontroluj(nazov, podmienka):
    """Zapise vysledok jedneho testu a vypise PASS/FAIL."""
    vysledky.append(bool(podmienka))
    print(("[PASS] " if podmienka else "[FAIL] ") + nazov)


def nova_db():
    """Vytvori cistu docasnu databazu v pamati (pre kazdy test zvlast)."""
    conn = databaza.pripoj(":memory:")
    databaza.vytvor_tabulku(conn)
    return conn


# --- Test 1: logika - parsovanie sumy ---
skontroluj("parsuj_sumu('10') = 10.0", logika.parsuj_sumu("10") == 10.0)
skontroluj("parsuj_sumu('4,50') = 4.5 (ciarka)", logika.parsuj_sumu("4,50") == 4.5)
skontroluj("parsuj_sumu('abc') = None", logika.parsuj_sumu("abc") is None)

# --- Test 2: databaza - pridanie a vypis ---
conn = nova_db()
databaza.pridaj_vydavok(conn, 4.50, "jedlo", "2026-06-03", "obed")
databaza.pridaj_vydavok(conn, 12.0, "doprava", "2026-05-20", "")
riadky = databaza.vsetky_vydavky(conn)
skontroluj("pridanie ulozi dva vydavky", len(riadky) == 2)
# vsetky_vydavky zoradzuje podla datumu, preto nekontrolujeme poradie, ale obe sumy:
sumy = sorted(r[1] for r in riadky)
skontroluj("ulozene sumy su 4.50 a 12.0", sumy == [4.50, 12.0])

# --- Test 3: prehlad spolu (SUM) ---
skontroluj("sucet vsetkych = 16.5", databaza.sucet_vsetkych(conn) == 16.5)
skontroluj("sucet prazdnej databazy = 0", databaza.sucet_vsetkych(nova_db()) == 0)

# --- Test 4: prehlad podla kategorie (GROUP BY) ---
conn2 = nova_db()
databaza.pridaj_vydavok(conn2, 4.0, "jedlo", "2026-06-01", "")
databaza.pridaj_vydavok(conn2, 6.0, "jedlo", "2026-06-02", "")
databaza.pridaj_vydavok(conn2, 12.0, "doprava", "2026-06-03", "")
podla_kat = dict(databaza.sucet_podla_kategorie(conn2))
skontroluj("jedlo spolu = 10.0", podla_kat["jedlo"] == 10.0)
skontroluj("doprava spolu = 12.0", podla_kat["doprava"] == 12.0)

# --- Test 5: prehlad za mesiac (WHERE ... LIKE) ---
skontroluj("za 2026-06 = 22.0 (vsetky)", databaza.sucet_za_mesiac(conn2, "2026-06") == 22.0)
skontroluj("za 2026-05 = 0 (nic)", databaza.sucet_za_mesiac(conn2, "2026-05") == 0)

# --- Test 6: mazanie (DELETE) ---
conn3 = nova_db()
databaza.pridaj_vydavok(conn3, 4.0, "jedlo", "2026-06-01", "")
databaza.pridaj_vydavok(conn3, 12.0, "doprava", "2026-06-02", "")
id_prveho = databaza.vsetky_vydavky(conn3)[0][0]
databaza.zmaz_vydavok(conn3, id_prveho)
zostatok = databaza.vsetky_vydavky(conn3)
skontroluj("po zmazani zostal 1 vydavok", len(zostatok) == 1)
skontroluj("zmazany spravny (zostala doprava)", zostatok[0][2] == "doprava")

# --- Test 7: vydavok podla id + uprava (UPDATE) ---
conn4 = nova_db()
databaza.pridaj_vydavok(conn4, 4.0, "jedlo", "2026-06-01", "obed")
id_v = databaza.vsetky_vydavky(conn4)[0][0]
najdeny = databaza.vydavok_podla_id(conn4, id_v)
skontroluj("vydavok_podla_id najde spravny zaznam", najdeny[2] == "jedlo")
skontroluj("vydavok_podla_id pre neexistujuce id vrati None", databaza.vydavok_podla_id(conn4, 999) is None)
databaza.uprav_vydavok(conn4, id_v, 9.99, "kava", "2026-06-05", "zmenene")
po_uprave = databaza.vydavok_podla_id(conn4, id_v)
skontroluj("uprava zmenila sumu na 9.99", po_uprave[1] == 9.99)
skontroluj("uprava zmenila kategoriu na kava", po_uprave[2] == "kava")

# --- Test 8: filter podla kategorie (WHERE kategoria) ---
conn5 = nova_db()
databaza.pridaj_vydavok(conn5, 4.0, "jedlo", "2026-06-01", "")
databaza.pridaj_vydavok(conn5, 6.0, "jedlo", "2026-06-02", "")
databaza.pridaj_vydavok(conn5, 12.0, "doprava", "2026-06-03", "")
len_jedlo = databaza.vydavky_v_kategorii(conn5, "jedlo")
skontroluj("filter 'jedlo' vrati 2 zaznamy", len(len_jedlo) == 2)
skontroluj("filter vrati len kategoriu jedlo", all(r[2] == "jedlo" for r in len_jedlo))


# --- Suhrn ---
print("-" * 40)
preslo = sum(vysledky)
spolu = len(vysledky)
if preslo == spolu:
    print(f"VYSLEDOK: vsetkych {spolu} testov PRESLO.")
else:
    print(f"VYSLEDOK: {preslo}/{spolu} preslo, {spolu - preslo} ZLYHALO.")
