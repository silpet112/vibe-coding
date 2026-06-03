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


def zmaz_vydavok(conn, id_vydavku):
    """Zmaze vydavok s danym id. SQL prikaz: DELETE."""
    conn.execute("DELETE FROM vydavky WHERE id = ?", (id_vydavku,))
    conn.commit()


def vydavok_podla_id(conn, id_vydavku):
    """Vrati jeden vydavok podla id (alebo None, ak neexistuje). SQL: SELECT ... WHERE id."""
    kurzor = conn.execute(
        "SELECT id, suma, kategoria, datum, poznamka FROM vydavky WHERE id = ?",
        (id_vydavku,),
    )
    return kurzor.fetchone()


def uprav_vydavok(conn, id_vydavku, suma, kategoria, datum, poznamka):
    """Prepise existujuci vydavok novymi hodnotami. SQL prikaz: UPDATE."""
    conn.execute(
        "UPDATE vydavky SET suma = ?, kategoria = ?, datum = ?, poznamka = ? WHERE id = ?",
        (suma, kategoria, datum, poznamka, id_vydavku),
    )
    conn.commit()


# --- Prehlady (databaza pocita za nas: SUM, GROUP BY) ---

def sucet_vsetkych(conn):
    """Vrati sucet vsetkych vydavkov (0, ak nic nie je). SQL: SUM."""
    kurzor = conn.execute("SELECT SUM(suma) FROM vydavky")
    vysledok = kurzor.fetchone()[0]
    return vysledok if vysledok is not None else 0


def sucet_podla_kategorie(conn):
    """Vrati zoznam (kategoria, sucet) zoradeny od najvacsej sumy. SQL: GROUP BY."""
    kurzor = conn.execute(
        "SELECT kategoria, SUM(suma) FROM vydavky GROUP BY kategoria ORDER BY SUM(suma) DESC"
    )
    return kurzor.fetchall()


def sucet_za_mesiac(conn, rok_mesiac):
    """Vrati sucet vydavkov za dany mesiac (rok_mesiac vo formate 'RRRR-MM').
    SQL: WHERE datum LIKE 'RRRR-MM%'."""
    kurzor = conn.execute(
        "SELECT SUM(suma) FROM vydavky WHERE datum LIKE ?",
        (rok_mesiac + "%",),
    )
    vysledok = kurzor.fetchone()[0]
    return vysledok if vysledok is not None else 0
