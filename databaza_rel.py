# databaza_rel.py - Projekt 8: RELACNA verzia datovej vrstvy vydavkov.
# Dve PREPOJENE tabulky: kategorie (zoznam) + vydavky (odkazuju na kategoriu cez kategoria_id).
# Je to samostatne (vlastny subor vydavky_rel.db), aby sme nepokazili povodnu databaza.py.

import sqlite3

SUBOR_DB = "vydavky_rel.db"


def pripoj(subor=SUBOR_DB):
    """Otvori spojenie a zapne kontrolu cudzich klucov (v SQLite je defaultne vypnuta)."""
    conn = sqlite3.connect(subor)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def vytvor_tabulky(conn):
    """Vytvori obe prepojene tabulky, ak este neexistuju."""
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS kategorie (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nazov TEXT NOT NULL UNIQUE
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS vydavky (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            suma REAL NOT NULL,
            kategoria_id INTEGER NOT NULL,
            datum TEXT NOT NULL,
            poznamka TEXT,
            FOREIGN KEY (kategoria_id) REFERENCES kategorie(id)
        )
        """
    )
    conn.commit()


# --- Kategorie ---

def id_kategorie(conn, nazov):
    """Vrati id kategorie podla nazvu; ak este neexistuje, vytvori ju a vrati nove id.
    Najprv pozrieme, ci uz existuje (aby sme zbytocne neminuli cislo id)."""
    riadok = conn.execute("SELECT id FROM kategorie WHERE nazov = ?", (nazov,)).fetchone()
    if riadok:
        return riadok[0]
    kurzor = conn.execute("INSERT INTO kategorie (nazov) VALUES (?)", (nazov,))
    conn.commit()
    return kurzor.lastrowid


def vsetky_kategorie(conn):
    """Vrati zoznam (id, nazov) vsetkych kategorii."""
    return conn.execute("SELECT id, nazov FROM kategorie ORDER BY nazov").fetchall()


# --- Vydavky ---

def pridaj_vydavok(conn, suma, kategoria_nazov, datum, poznamka):
    """Prida vydavok. Kategoriu zadavame NAZVOM - funkcia si najde/vytvori jej id (cudzi kluc)."""
    kid = id_kategorie(conn, kategoria_nazov)
    conn.execute(
        "INSERT INTO vydavky (suma, kategoria_id, datum, poznamka) VALUES (?, ?, ?, ?)",
        (suma, kid, datum, poznamka),
    )
    conn.commit()


def vsetky_vydavky(conn):
    """Vrati vydavky aj s NAZVOM kategorie - cez JOIN spoji obe tabulky."""
    return conn.execute(
        """
        SELECT vydavky.id, vydavky.suma, kategorie.nazov, vydavky.datum, vydavky.poznamka
        FROM vydavky
        JOIN kategorie ON vydavky.kategoria_id = kategorie.id
        ORDER BY vydavky.datum
        """
    ).fetchall()


def sucet_podla_kategorie(conn):
    """Sucet vydavkov podla kategorie - JOIN + GROUP BY."""
    return conn.execute(
        """
        SELECT kategorie.nazov, SUM(vydavky.suma)
        FROM vydavky
        JOIN kategorie ON vydavky.kategoria_id = kategorie.id
        GROUP BY kategorie.nazov
        ORDER BY SUM(vydavky.suma) DESC
        """
    ).fetchall()
