# databaza.py - vrstva DATABAZA: vsetka praca so SQLite (pripojenie + SQL prikazy).
# Ina vrstva sa nemusi starat o SQL - len zavola tieto funkcie.

import sqlite3

from konfig import SUBOR_DB


def pripoj(subor=SUBOR_DB):
    """Otvori (alebo vytvori) databazovy subor a vrati spojenie.
    Da sa zadat iny subor (vyuzije sa v testoch s docasnou DB)."""
    return sqlite3.connect(subor)


def vytvor_tabulku(conn):
    """Vytvori tabulku 'vydavky', ak este neexistuje.
    Stlpce: id (samo sa cisluje), suma, kategoria, datum, poznamka."""
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS vydavky (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            suma REAL NOT NULL,
            kategoria TEXT NOT NULL,
            datum TEXT NOT NULL,
            poznamka TEXT
        )
        """
    )
    conn.commit()


def pridaj_vydavok(conn, suma, kategoria, datum, poznamka):
    """Prida jeden vydavok (jeden riadok) do tabulky. SQL prikaz: INSERT."""
    conn.execute(
        "INSERT INTO vydavky (suma, kategoria, datum, poznamka) VALUES (?, ?, ?, ?)",
        (suma, kategoria, datum, poznamka),
    )
    conn.commit()


def vsetky_vydavky(conn):
    """Vrati vsetky vydavky ako zoznam riadkov. SQL prikaz: SELECT."""
    kurzor = conn.execute(
        "SELECT id, suma, kategoria, datum, poznamka FROM vydavky ORDER BY datum"
    )
    return kurzor.fetchall()
