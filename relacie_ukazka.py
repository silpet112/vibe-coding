# relacie_ukazka.py - Projekt 8, Etapa 1: ukazka PREPOJENYCH tabuliek (relacie + JOIN).
# Spustenie:  python relacie_ukazka.py
# Databaza bezi V PAMATI (':memory:') - cisto na ucenie, nic sa neuklada.

import sqlite3

conn = sqlite3.connect(":memory:")

# 1) Tabulka kategorii: kazda kategoria RAZ, s vlastnym id a nazvom.
conn.execute("""
    CREATE TABLE kategorie (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nazov TEXT NOT NULL UNIQUE
    )
""")

# 2) Tabulka vydavkov: namiesto textu drzi 'kategoria_id', ktore ODKAZUJE na kategorie.id.
#    Tomuto odkazu sa hovori CUDZI KLUC (foreign key).
conn.execute("""
    CREATE TABLE vydavky (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        suma REAL NOT NULL,
        kategoria_id INTEGER NOT NULL,
        FOREIGN KEY (kategoria_id) REFERENCES kategorie(id)
    )
""")

# Naplnime kategorie (jedlo dostane id=1, doprava id=2) a par vydavkov.
conn.execute("INSERT INTO kategorie (nazov) VALUES ('jedlo'), ('doprava')")
conn.execute("INSERT INTO vydavky (suma, kategoria_id) VALUES (4.5, 1), (6.0, 1), (12.0, 2)")
conn.commit()

print("=== Vydavky s nazvom kategorie (cez JOIN) ===")
# JOIN spoji riadky z dvoch tabuliek tam, kde vydavky.kategoria_id == kategorie.id
for r in conn.execute("""
    SELECT vydavky.id, vydavky.suma, kategorie.nazov
    FROM vydavky
    JOIN kategorie ON vydavky.kategoria_id = kategorie.id
    ORDER BY vydavky.id
"""):
    print(f"  #{r[0]}  {r[1]:.2f}  [{r[2]}]")

print("\n=== Sucet podla kategorie (JOIN + GROUP BY) ===")
for r in conn.execute("""
    SELECT kategorie.nazov, SUM(vydavky.suma)
    FROM vydavky
    JOIN kategorie ON vydavky.kategoria_id = kategorie.id
    GROUP BY kategorie.nazov
    ORDER BY SUM(vydavky.suma) DESC
"""):
    print(f"  {r[0]:<10} {r[1]:.2f}")

conn.close()
