# test_todo.py - jednoduche automaticke testy pre todo.py
# Spustenie:  python test_todo.py
# Testujeme "cistu logiku" z todo.py (ziadny input ani subor).

import todo

vysledky = []


def skontroluj(nazov, podmienka):
    """Zapise vysledok jedneho testu a vypise PASS/FAIL."""
    vysledky.append(bool(podmienka))
    print(("[PASS] " if podmienka else "[FAIL] ") + nazov)


# --- Test 1: pridanie ulohy ---
ulohy = []
todo.pridaj_ulohu(ulohy, "Kupit mlieko")
skontroluj("pridanie prida jednu ulohu", len(ulohy) == 1)
skontroluj("nova uloha ma spravny text", ulohy[0]["text"] == "Kupit mlieko")
skontroluj("nova uloha nie je hotova", ulohy[0]["hotovo"] is False)
skontroluj("nova uloha nie je prioritna", ulohy[0]["priorita"] is False)

# --- Test 2: oznacenie ako hotove ---
todo.oznac_ako_hotovu(ulohy, 0)
skontroluj("oznacenie nastavi hotovo na True", ulohy[0]["hotovo"] is True)

# --- Test 3: priorita (prepnutie tam a spat) ---
stav1 = todo.prepni_prioritu(ulohy, 0)
skontroluj("prve prepnutie zapne prioritu", stav1 is True and ulohy[0]["priorita"] is True)
stav2 = todo.prepni_prioritu(ulohy, 0)
skontroluj("druhe prepnutie vypne prioritu", stav2 is False and ulohy[0]["priorita"] is False)

# --- Test 4: zmazanie ---
todo.pridaj_ulohu(ulohy, "Druha uloha")
pocet_pred = len(ulohy)
todo.zmaz_ulohu(ulohy, 0)
skontroluj("zmazanie znizi pocet o 1", len(ulohy) == pocet_pred - 1)
skontroluj("ostala spravna uloha", ulohy[0]["text"] == "Druha uloha")


# --- Suhrn ---
print("-" * 32)
preslo = sum(vysledky)
spolu = len(vysledky)
if preslo == spolu:
    print(f"VYSLEDOK: vsetkych {spolu} testov PRESLO.")
else:
    print(f"VYSLEDOK: {preslo}/{spolu} preslo, {spolu - preslo} ZLYHALO.")
