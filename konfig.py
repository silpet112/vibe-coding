# konfig.py - vrstva NASTAVENIA: nacita hodnoty zo suboru .env (mimo kodu).
# Ostatne vrstvy si odtialto beru SUBOR_DB a MENA.

import os
from dotenv import load_dotenv

load_dotenv()  # nacita .env, ak existuje

SUBOR_DB = os.getenv("DB_SUBOR", "vydavky.db")  # nazov suboru s databazou
MENA = os.getenv("MENA", "EUR")                 # mena pre vypis (napr. EUR, CZK)
