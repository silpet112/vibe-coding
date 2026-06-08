# API — MAPA 🗺️🔌
### Tvoja referencia / „učebnica" o API (ako appka získava dáta z internetu)

> Toto je text na **čítanie a opakovanie**. Nemusíš sa to učiť naspamäť — prejdeme si to naživo
> na Projekte 6 (Počasie). Kedykoľvek sa sem vieš vrátiť a pozrieť, „ako to bolo".
>
> Postup a zaškrtávanie pokroku je v **POKROK.md**. Recept na stavanie je v **STAVANIE-S-AI.md**.

---

## Čo je API (jednoducho) 🟢

**API** = *Application Programming Interface*. Po slovensky: **dohodnutý spôsob, ako sa dva programy
medzi sebou rozprávajú.** Je to ako **čašník v reštaurácii**:

- Ty (tvoj program) si **objednáš** (pošleš *požiadavku*).
- Kuchyňa (cudzí server, napr. počasie) **pripraví** odpoveď.
- Čašník (API) ti **prinesie** výsledok (dáta).

Nemusíš vedieť, *ako* kuchyňa varí — stačí poznať **jedálny lístok** (čo si vieš vypýtať a v akom tvare to príde).

**Príklad z bežného života:** appka na počasie v telefóne nemá v sebe počasie celého sveta —
**pýta si ho cez API** od služby, ktorá ho meria. Tvoja appka bude robiť presne to isté.

---

## Ako to funguje: požiadavka → odpoveď 🟢

```
TVOJ PROGRAM  ──(požiadavka na adresu/URL)──▶  SERVER API
TVOJ PROGRAM  ◀──(odpoveď: dáta v JSON)──────  SERVER API
```

1. Program pošle **požiadavku (request)** na konkrétnu **adresu (URL / endpoint)**.
2. Server vráti **odpoveď (response)** — väčšinou dáta vo formáte **JSON**.
3. Program si z JSON **vytiahne** to, čo potrebuje (napr. teplotu).

---

## Kľúčové pojmy 🟢

| Pojem | Čo znamená (jednoducho) |
|---|---|
| **API** | Dohodnutý spôsob, ako si programy posielajú dáta. |
| **Endpoint / URL** | Presná adresa, na ktorú posielam požiadavku (napr. `https://api.open-meteo.com/v1/forecast`). |
| **Požiadavka (request)** | „Otázka", ktorú pošlem serveru. |
| **Odpoveď (response)** | „Odpoveď" servera — zvyčajne dáta v JSON. |
| **JSON** | Textový formát dát: dvojice `"kľúč": hodnota`, zoznamy `[...]`, objekty `{...}`. Vyzerá skoro ako Python slovník. |
| **Parameter (query string)** | Spresnenie požiadavky v adrese za `?` (napr. `?latitude=48.1&longitude=17.1`). Poznáš z filtra vo výdavkoch! |
| **HTTP metóda** | `GET` = daj mi dáta (čítanie), `POST` = pošli dáta. Pri čítaní z API väčšinou **GET**. |
| **Stavový kód (status)** | Číslo, či to vyšlo: **200** = OK, **404** = nenájdené, **500** = chyba servera. |
| **API kľúč (key)** | Heslo/lístok, ktorým sa pri niektorých API preukážeš. **Tajné** → patrí do `.env` (poznáš z Projektu 3!). |
| **Rate limit** | Koľko požiadaviek smieš poslať za čas (aby si server nezahltil). |

> 💡 Open-Meteo (počasie), ktoré použijeme, **nepotrebuje API kľúč** — je zadarmo. Preto sa môžeme
> sústrediť na podstatu a netrápiť sa s registráciou.

---

## Ako sa API volá v Pythone 🔵

Na posielanie požiadaviek slúži balíček **`requests`** (doinštalujeme `pip install requests`):

```python
import requests

# 1) pošli GET požiadavku na adresu s parametrami
odpoved = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": 48.15, "longitude": 17.11, "current": "temperature_2m"},
)

# 2) skontroluj, či to vyšlo (200 = OK)
print(odpoved.status_code)

# 3) preveď odpoveď z JSON na Python slovník a vytiahni dáta
data = odpoved.json()
print(data["current"]["temperature_2m"])
```

To je celé jadro práce s API: **adresa + parametre → odpoveď → vytiahni z JSON to svoje.**

---

## Ako to spojíme s tým, čo už vieš 🔵

- **Parametre v adrese** (`?latitude=…`) — to isté ako filter `?kategoria=…` z výdavkovej appky.
- **JSON** — podobné slovníku; dáta sme ukladali aj v `ulohy.json` (Projekt 1).
- **API kľúč → `.env`** — tajomstvá mimo kódu (Projekt 3).
- **Oddelenie vrstiev** — „získať dáta z API" (jedna funkcia) oddelíme od „spracovať/zobraziť" (ďalšia),
  presne ako `databaza` vs `logika`. Vďaka tomu sa to dá aj **testovať**.
- **Web (Flask)** — výsledok z API vieme neskôr ukázať aj na **stránke**.

---

## Na čo si dať pozor 🟣

- **Internet je potrebný** — bez pripojenia API nezavoláš; program má pekne ošetriť chybu (nie spadnúť).
- **Cudzí server môže zlyhať** alebo vrátiť **404** (napr. mesto nenájdené) — vždy skontroluj stav/odpoveď.
- **Kľúče nikdy do gitu** — len do `.env` (a `.env` do `.gitignore`).
- **Formát odpovede sa môže líšiť** — preto sa v dokumentácii API pozeráš, ako JSON vyzerá.

---

## Pár verejných API zadarmo (na hranie) 🟢

| API | Čo dáva | Kľúč? |
|---|---|---|
| **Open-Meteo** | počasie podľa súradníc | nie 🎉 (toto použijeme) |
| **Open-Meteo Geocoding** | súradnice podľa názvu mesta | nie |
| **Frankfurter** | kurzy mien | nie |
| **REST Countries** | info o krajinách | nie |

---

## Projekt 6 — Počasie (čo postavíme) 🌦️

Malá appka: **zadáš mesto → appka cez API zistí počasie a vypíše ho.** Postupne (po etapách)
sa naučíš celý kolobeh práce s API — od prvého volania až po pekný, „nespadnuteľný" program.
Detailný postup a etapy sú v **POKROK.md**.
