# hesla_ukazka.py - Projekt 10, Etapa 1: preco a ako sa HASHUJU hesla.
# Spustenie:  python hesla_ukazka.py
# Pouzivame werkzeug (subor Flasku) - netreba nic instalovat.

from werkzeug.security import generate_password_hash, check_password_hash

heslo = "tajne123"

# Heslo premenime na "hash" - necitatelny odtlacok, ktory sa NEDA vratit spat na heslo.
hash_hesla = generate_password_hash(heslo)
print("Povodne heslo:  ", heslo)
print("Ulozeny hash:   ", hash_hesla)
print()

# Pri prihlaseni neporovnavame hesla, ale overime hash:
print("Spravne heslo ('tajne123') sedi? ", check_password_hash(hash_hesla, "tajne123"))
print("Zle heslo ('hacker') sedi?       ", check_password_hash(hash_hesla, "hacker"))
print()

# To iste heslo -> zakazdym INY hash (vdaka nahodnej 'soli'/salt), ale oba overia spravne heslo.
hash2 = generate_password_hash(heslo)
print("Druhy hash je iny ako prvy?      ", hash2 != hash_hesla)
print("Aj druhy hash overi spravne heslo?", check_password_hash(hash2, "tajne123"))
