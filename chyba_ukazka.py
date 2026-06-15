# chyba_ukazka.py - Projekt 11, Etapa 2: ucime sa CITAT chybu (traceback).
# Tento subor ma NASCHVAL chybu - spustime ho, precitame traceback a opravime.

def priemer(cisla):
    return sum(cisla) / len(cisla)


def spracuj(udaje):
    # vytiahne zoznam hodnot a vrati ich priemer
    return priemer(udaje["hodnoty"])


data = {"nazov": "test", "hodnoty": [2, 4, 6]}   # OPRAVENE: doplneny kluc "hodnoty"
print("Priemer je:", spracuj(data))
