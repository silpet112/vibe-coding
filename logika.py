# logika.py - vrstva LOGIKA: ciste vypocty a spracovanie (ziadny input, vypis ani databaza).
# Vdaka tomu sa da lahko testovat (Etapa E). Zatial obsahuje spracovanie sumy;
# v Etape D sem pribudnu prehlady (sucty).


def parsuj_sumu(text):
    """Prevedie text na cislo (akceptuje ciarku); vrati None, ak to nie je platne cislo."""
    text = text.strip().replace(",", ".")
    try:
        return float(text)
    except ValueError:
        return None
