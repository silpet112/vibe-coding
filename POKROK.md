# POKROK — môj denník učenia

> Tento súbor je môj prehľad o tom, čo som sa už naučil a kde som skončil.
> Mentor ho po každej lekcii aktualizuje, aby sme nabudúce hneď nadviazali.

---

## Ako sa tento súbor používa
- Na **konci každej lekcie** mentor doplní nový záznam do sekcie „Denník lekcií".
- Mentor priebežne udržiava sekciu **„Kde som teraz"**, aby bolo jasné,
  čím začať budúci raz.
- Keď niečo naozaj ovládam, presunie sa to do **„Čo už ovládam"**.
- Keď na niečo natrafíme a treba sa k tomu vrátiť, zapíše sa to do **„Na zopakovanie"**.

---

## Kde som teraz
**Aktuálna téma:** 🌐 Projekt 9 — Vlastný API + JavaScript (modul I): Flask vracia JSON, stránka cez `fetch`
**Posledná lekcia:** Etapa 3 — **kalkulačka cez API** (`/api/vypocet` +,−,×,÷, znova použitá `kalkulacka.py`) + výber operácie a Enter, overené ✅
**Ďalší krok:** Etapa 4 — **testy** API + **uzavrieť Projekt 9**. Mapa: [VIBE-CODING-MAPA.md](VIBE-CODING-MAPA.md) (modul I)
**Mapy/referencie:** [API-MAPA.md](API-MAPA.md) · [VIBE-CODING-MAPA.md](VIBE-CODING-MAPA.md) (zostávajúce lekcie F–L) · [STAVANIE-S-AI.md](STAVANIE-S-AI.md)

> Pozn.: Kurz Claude Code (A1–E20) je **hotový**. Teraz sme na ceste **„Stavanie s AI"** (cieľ:
> stavať projekty, kde som režisér). Programovacia osnova (1–10) ostáva zaparkovaná na neskôr.

---

## Čo už ovládam
*(Sem mentor pridáva pojmy a zručnosti, ktoré som si naozaj osvojil.)*

- **Claude Code = agent, nie chatbot** — vykonáva zadané úlohy (sám číta a mení súbory,
  spúšťa príkazy), pričom ho usmerňujem a schvaľujem; chatbot iba vysvetľuje/odpovedá.
- **Agentický cyklus**: získa kontext → koná → overí. Brzda = **Esc**.
- **Rozhranie**: turn (kolo) = jedna výmena; *tool use* = viditeľný krok „Read…" keď čítam
  súbory; *diff* = 🟩 pridané / 🟥 zmazané (vidím pred schválením); **Shift+Enter** = nový riadok.
- **Režimy povolení** (Shift+Tab): *ask before edits* (Default, najbezpečnejší) · *edit
  automatically* (accept edits) · *plan mode* · *auto mode* (pokročilý). Na štart = Default.
- **Súbory a kontext**: súbor pridám cez **@** (vyskočí zoznam); *kontext* = pamäť rozhovoru
  (obmedzená, meraná v tokenoch); `/context` ukáže využitie; `/clear` vyčistí (medzi témami).
- **Slash príkazy**: príkazy pre Claude Code (`/`); `/help` (zoznam), `/model` (prepnúť mozog —
  Opus/Sonnet/Haiku), `/config` (klikacie nastavenia → súbor settings.json).
- **CLAUDE.md = pamäť projektu**: Claude ho číta na začiatku každého sedenia; drží sa krátky;
  `/init` ho vygeneruje. (Mám vytvorený vlastný CLAUDE.md pre tento priečinok.)
- **Prompting (zadávanie úloh)**: 4 pravidlá — buď konkrétny, daj príklad, žiadaj overenie,
  iteruj; mysli ako pri delegovaní kolegovi.
- **Plánovací režim (explore → plan → code → over)**: pri väčšej úlohe najprv plán na
  schválenie, žiadny kód; potom vykonať a overiť. Vyskúšané na vlastnom programe `faktorial.ps1`.
- **Rewind / checkpointy**: Claude si pri každom prompte uloží snímku; cez `/rewind` alebo
  **Esc Esc** sa viem vrátiť späť (napr. „vrátiť kód"). Vďaka tomu môžem bez strachu experimentovať.
- **Sedenia (sessions)**: každý rozhovor sa ukladá; `/resume` (pokračovať v staršom), `/clear`
  (nová téma); jedna téma = jedno sedenie. (`/rename` v tomto prostredí nie je dostupný.)
- **VS Code integrácia**: panel, inline diffy, **výber textu = kontext** (Claude vidí, čo
  označím), @-odkazy s riadkami (`@subor#5-10`), skratky (Ctrl+Esc, Alt+K, Shift+Enter, Ctrl+G).
- **Git (základ)**: systém histórie verzií; *commit* = uložená verzia s popisom; *repo*, *diff*,
  *vetva*; Claude vie commitovať/vetviť; `/review` a `/code-review` kontrolujú zmeny.
  *Git nainštalovaný (winget, v2.54), repo založené, prvý commit hotový: `git init` → `git add -A` → `git commit -m`.*
- **settings.json**: súbor za `/config`; `permissions` (allow/deny/ask), `defaultMode`, model, env;
  3 miesta (user `~/.claude/`, projekt `.claude/`, local `.claude/settings.local.json`).
  Allow-rule = vopred povolená akcia (môže mať wildcard `*`, napr. `Bash(git *)`).
- **Skills (vlastné príkazy)**: postup v `.claude/skills/názov/SKILL.md` (frontmatter `name`+`description`
  + telo s inštrukciami); vyvolá sa `/názov`; načíta sa až keď treba. Mám vytvorený vlastný `/pokracuj`.
- **Subagenty**: samostatný Claude na vedľajšiu úlohu vo vlastnej pamäti (vráti len zhrnutie, šetrí
  kontext); typy Explore/Plan/general-purpose; vlastné v `.claude/agents/`; dajú sa púšťať paralelne.
- **MCP servery**: „zásuvka" na pripojenie externých nástrojov (Gmail, Kalendár, Drive, Notion,
  ClickUp…); Claude s nimi vie reálne pracovať; pridanie `claude mcp add` / konektory. Mám viaceré pripojené.
- **Vlastné skilly v praxi**: vytvoril som si `/pod` a `/pokracuj` (po reštarte fungujú).
- **Hooks**: príkaz, ktorý sa spustí automaticky a deterministicky pri udalosti (napr. po úprave
  súboru); na rozdiel od CLAUDE.md (odporúčanie) ho program vykoná **vždy**; nastavuje sa v `settings.json`.
- **Workflowy**: Claude riadi veľa agentov naraz podľa skriptu — na veľké úlohy (migrácie,
  audity, dôkladný research); spustí sa slovami, sleduje cez `/workflows`. (Subagent = 1, workflow = tím.)
- **Plánovanie v čase**: `/loop` (opakuj úlohu počas sedenia), naplánované úlohy/routines (bežia
  „v oblaku" aj bez teba/PC), pripomienky (jednorazovo neskôr).
- **Najlepšie návyky**: (1) spravuj kontext (`/clear`), (2) vždy over, (3) najprv plán, (4) buď
  konkrétny + príklad, (5) oprav skoro; bonus writer/reviewer (kontrola v čistom rozhovore).
- **Stavanie s AI — scoping**: zadefinovať víziu (1 veta) a **MVP** (najmenšia užitočná verzia);
  pre prvú verziu radšej menej funkcií, zvyšok doplniť iteráciami.
- **Stavanie s AI — postav → spusti → over → commit**: necháš Claude postaviť MVP, **sám spustíš
  a overíš**, fungujúcu verziu uložíš commitom; verzionuj kód (`todo.py`), nie dáta (`ulohy.json` v `.gitignore`).
- **Stavanie s AI — iterácia**: appku používaš, **konkrétne zadáš jedno vylepšenie naraz**, overíš
  a commitneš; takto appka rastie podľa teba (napr. pridané mazanie úloh s potvrdením).
- **Stavanie s AI — debugging**: chybu nemusím opraviť sám — **jasne ju opíšem** (čo čakám / čo sa
  deje / ako zopakovať), Claude opraví, ja overím; záchranné siete = commit + `/rewind`.
- **Kontext — compact**: `/compact` zhrnie rozhovor a uvoľní pamäť (pri ~100% sa to deje aj samo,
  nespadne to); detaily zo začiatku sa môžu stratiť → dôležité držím v súboroch (POKROK.md, git).
- **Stavanie s AI — vyladenie + „kedy je hotovo"**: pridať čerešničku (napr. priorita = farebný text
  v termináli cez ANSI), ale vedieť projekt **včas uzavrieť** (vyhnúť sa feature-creep).
- **Režisérsky recept (na akýkoľvek projekt)** ⭐: Vízia → MVP → Plán → Postav → Spusti & over →
  Commit → Iteruj → uzavri. Viem ho zopakovať sám (overené na projekte Správca úloh).
- **Automatické testy**: samostatný program (`test_todo.py`), čo sám overí logiku appky a hlási
  PASS/FAIL; chytí chyby za mňa pred zmenami. Podmienka: oddeliť čistú logiku od obsluhy (input/výpis).
- **Databáza (SQLite)**: dáta v *tabuľke* (riadky = záznamy, stĺpce = polia), ovládaná príkazmi
  **SQL** (`INSERT` pridaj, `SELECT` vyber). SQLite je vstavaná v Pythone (`import sqlite3`), celá
  v jednom súbore (`vydavky.db`); lepšia než JSON pri raste dát. Dátový súbor → `.gitignore` (`*.db`).
- **.env (konfigurácia mimo kódu)**: nastavenia/tajomstvá v súbore `.env` (`KLÚČ=hodnota`), načítané
  cez `python-dotenv` (`load_dotenv()` + `os.getenv()`). `.env` → `.gitignore` (nepatrí do gitu);
  do gitu ide len vzor `.env.example`. Mením správanie appky bez zásahu do kódu.
- **pip install**: doinštalovanie hotového balíčka od niekoho iného: `python -m pip install názov`
  (napr. `python-dotenv`). Potom ho v kóde použijem cez `import`.
- **Architektúra (vrstvy)**: appku rozdelím na súbory, každý s jednou zodpovednosťou — `konfig.py`
  (nastavenia), `databaza.py` (SQL/úložisko), `logika.py` (čisté výpočty), `vydavky.py` (menu/obsluha).
  Súbory sa prepájajú cez `import`. Výhoda: prehľadnosť, ľahšie hľadanie chýb, testovateľné vrstvy.
- **SQL prehľady (agregácia)**: databáza počíta za mňa — `SUM(stĺpec)` (súčet), `GROUP BY` (zoskup
  a spočítaj po skupinách), `WHERE ... LIKE 'RRRR-MM%'` (filter, napr. za mesiac). Toto je hlavná
  výhoda databázy oproti zoznamu: rýchle súčty/filtre aj nad množstvom dát.
- **Testy s dočasnou databázou**: testy bežia na DB v pamäti (`sqlite3` `':memory:'`), aby sa
  nedotkli reálnych dát; po teste zmizne. Možné vďaka tomu, že `pripoj()` prijíma názov DB (výhoda
  vrstvenej architektúry). Test môže odhaliť aj zlý predpoklad v samotnom teste, nielen v kóde.
- **Web (Flask základ)**: appka v prehliadači. **Server** beží na mojom počítači
  (`http://127.0.0.1:5000`), prehliadač mu posiela požiadavky; **route** (`@app.route("/")`) priradí
  funkciu k adrese a vráti stránku. Spustím `python app.py`, zastavím `Ctrl+C`. Inštalácia: `pip install flask`.
- **HTML šablóna (Jinja2)**: HTML súbor v `templates/`, do ktorého Flask dosadí dáta cez
  `render_template("subor.html", data=...)`. Značky: `{{ hodnota }}` vloží hodnotu, `{% for %}…{% endfor %}`
  opakuje (napr. riadky tabuľky). Web aj terminál čítajú z tej istej vrstvy `databaza.py` (sila architektúry).
- **Formulár / GET vs POST**: **GET** = vyžiadať stránku (čítanie), **POST** = poslať serveru dáta
  (`<form method="post">` + `<input name="...">`). Route s `methods=["POST"]` číta `request.form`,
  uloží a vráti `redirect(url_for(...))` (presmerovanie po odoslaní, aby F5 neodoslalo formulár znova).
- **CSS (vzhľad)**: HTML = *čo* je na stránke (obsah), CSS = *ako* to vyzerá (písmo, farby, rámčeky,
  odsadenie). Jednoduché štýly viem dať do `<style>` v hlavičke šablóny. Oddelenie obsahu od vzhľadu.
- **API (volanie dát z internetu)**: appka si cez **`requests.get(url, params=...)`** vypýta dáta od
  cudzej služby (endpoint), dostane **odpoveď** (stavový kód 200/404…), `.json()` ju premení na slovník
  a z neho vytiahnem hodnotu. JSON ≈ slovník; parametre `?a=b` ≈ filter z webu; kľúče → `.env`. Mapa: API-MAPA.md.
- **CRUD a SQL `DELETE`**: štyri základné operácie s dátami — Create (`INSERT`), Read (`SELECT`),
  Update (`UPDATE`), Delete (`DELETE`). `DELETE FROM ... WHERE id = ?` vymaže riadok. Route môže mať
  v adrese parameter (`/zmaz/<int:id>`); mazanie istím potvrdením v prehliadači (`confirm(...)`).
- **SQL `UPDATE` a úprava (edit)**: `UPDATE ... SET ... WHERE id = ?` prepíše záznam. Úprava má 2 kroky:
  GET ukáže formulár **predvyplnený** (`value="{{ ... }}"`), POST uloží. Tá istá route zvládne GET aj
  POST (`methods=["GET","POST"]`, vetvenie cez `request.method`). Tým mám kompletný CRUD na webe.
- **Query string (filter)**: dodatočné info v adrese za `?` (napr. `/?kategoria=jedlo`); vo Flasku
  cez `request.args.get("kategoria")`. Použité na filtrovanie zoznamu. V šablóne odkaz `?kategoria={{ x|urlencode }}`.
- **Vlastný skill `/app`**: skill, ktorý spustí Flask server na pozadí a otvorí appku v prehliadači
  (`Start-Process "http://127.0.0.1:5000"`) — jedným príkazom namiesto ručného spúšťania.

---

## Na zopakovanie
*(Veci, ktoré som už videl, ale ešte mi celkom nesadli — vrátime sa k nim.)*

- ~~Nainštalovať Python~~ — ✅ HOTOVO (2026-06-02, winget, Python 3.13.13). Funguje `python` aj `py`.
- ~~Nainštalovať Git~~ — ✅ HOTOVO (2026-06-02, winget v2.54); repo založené, prvý commit `554c82a`.

---

## Denník lekcií
*(Najnovší záznam navrch. Formát nižšie.)*

### Projekt 9 · Vlastný API + JavaScript — Etapa 3 (kalkulačka cez API) — 2026-06-11
**Čo sme prebrali:**
- Rozšírený API: `/api/vypocet?a=..&b=..&op=scitaj|odcitaj|nasob|delit` → JSON; **znova použité funkcie z `kalkulacka.py`** (Projekt 2), delenie nulou → 400 + chyba.
- Stránka: výber operácie (`<select>`) + počítanie aj cez **Enter** (`keydown`), JS volá `/api/vypocet`.

**Čo som dokázal:**
- Z ukážky vznikla **kalkulačka cez API** na webe (bez reloadu); pekné spojenie starých projektov. Commit `f694156`. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 4 — testy API (`/api/vypocet`) + uzavrieť Projekt 9.

### Projekt 9 · Vlastný API + JavaScript — Etapa 2 (fetch bez reloadu) — 2026-06-11
**Čo sme prebrali:**
- **JavaScript** beží v prehliadači a mení stránku za behu; **`fetch`** zavolá náš API a dostane JSON.
- `scitanie.html`: políčka a/b + tlačidlo → `fetch('/api/scitaj?a=..&b=..')` → výsledok sa **dopíše na stránku bez obnovenia**. Pridaná route `/` v `api_demo.py`.

**Čo som dokázal:**
- Zadal som čísla, klikol Spočítať a výsledok sa objavil hneď bez reloadu (chybný vstup → hláška). Commit `8a0620e`. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 3 — spojiť/vyladiť do mini-appky (živý výpočet), prípadne testy a uzavrieť.

### Projekt 9 · Vlastný API + JavaScript — Etapa 1 (vlastný API) — 2026-06-11
**Čo sme prebrali:**
- Rozdiel: Flask doteraz vracal **HTML stránky**; **API endpoint** vracia **JSON** (čisté dáta) cez `jsonify` — z toho sa stáva „tvoj vlastný API", ktorý vie použiť JavaScript/iná appka.
- `api_demo.py`: `/api/scitaj?a=..&b=..` vráti `{"sucet": ...}`; neplatný vstup → stav 400 + JSON s chybou. Port 5002.

**Čo som dokázal:**
- Otvoril som API v prehliadači a videl surové JSON dáta (nie stránku). Commit `cc8ea87`. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 2 — JavaScript `fetch`: stránka si vypýta dáta z API a ukáže výsledok bez obnovenia.

### Projekt 8 · Prepojené tabuľky — Etapa 4 (testy) + UZAVRETÝ 🏁 — 2026-06-11
**Čo sme prebrali:**
- Testy relačnej logiky `test_databaza_rel.py` (8/8 PASS, DB v pamäti): kategória sa **nezduplikuje** (rovnaké meno → rovnaké id), `JOIN` vráti **názov** kategórie, súčty podľa kategórie sedia.

**Čo som dokázal:**
- **Projekt 8 dokončený** — relačná DB (kategórie ako vlastná tabuľka, cudzí kľúč, `JOIN`) + menu + testy. Commit `e3e1b06`. 🎉

**Kde sme skončili / ďalší krok:**
- Projekt 8 uzavretý. Ďalej podľa [VIBE-CODING-MAPA.md](VIBE-CODING-MAPA.md): I (vlastný API + JS) / J (prihlasovanie) / K (venv + debugging), alebo pauza.

### Projekt 8 · Prepojené tabuľky — Etapa 3 (menu nad relačnou DB) — 2026-06-11
**Čo sme prebrali:**
- Terminálové menu `vydavky_rel.py` nad `databaza_rel.py`: pridať výdavok, zobraziť všetky (s názvom kategórie cez `JOIN`), prehľad podľa kategórie, zoznam kategórií.
- Znova použitá `logika.parsuj_sumu` z Projektu 3. Overené end-to-end (simulované vstupy).

**Čo som dokázal:**
- Celá relačná appka funguje od vstupu po výpis; tá istá kategória ostáva v tabuľke len raz (výhoda relácií). Commit `b2ad27b`. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 4 — testy relačnej logiky + uzavrieť Projekt 8.

### Projekt 8 · Prepojené tabuľky — Etapa 2 (relačná dátová vrstva) — 2026-06-11
**Čo sme prebrali:**
- Relačná verzia dátovej vrstvy `databaza_rel.py` (vlastný `vydavky_rel.db`, nech sa nepokazí pôvodná `databaza.py`).
- Tabuľky `kategorie` + `vydavky` (s `kategoria_id` = cudzí kľúč, `PRAGMA foreign_keys = ON`); `id_kategorie` nájde/vytvorí kategóriu, `pridaj_vydavok` berie názov kategórie a uloží jej id; `vsetky_vydavky` a `sucet_podla_kategorie` čítajú cez **`JOIN`**.

**Čo som dokázal:**
- Overené: výdavky sa ukladajú relačne (kategória ako id) a vypisujú aj s názvom cez JOIN; súčty sedia. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 3 — malé menu (rozhranie) nad `databaza_rel.py`.

### Projekt 8 · Prepojené tabuľky — Etapa 1 (relácie + JOIN) — 2026-06-11
**Čo sme prebrali:**
- Pojmy **relácia / cudzí kľúč (foreign key) / `JOIN`**: kategórie ako vlastná tabuľka (`kategorie`), výdavky držia len `kategoria_id`, ktoré odkazuje na `kategorie.id`.
- `JOIN ... ON vydavky.kategoria_id = kategorie.id` spojí tabuľky a dotiahne názov kategórie; `JOIN + GROUP BY` = súčet podľa kategórie.
- Ukázané na čistom príklade `relacie_ukazka.py` (DB v pamäti, nič sa neukladá).

**Čo som dokázal:**
- Videl som naživo, ako sa dve tabuľky prepoja cez `JOIN` (výdavky s názvom kategórie + súčty). ✅

**Kde sme skončili / ďalší krok:**
- Etapa 2 — zaviesť kategórie ako tabuľku priamo do `databaza.py` (pridať/vybrať + výpis cez JOIN).

### Projekt 7 · Nasadenie — Etapa 4 (produkčný server) + UZAVRETÝ 🏁 — 2026-06-11
**Čo sme prebrali:**
- Pojem **produkčný server**: `app.run(debug=True)` je len na vývoj; na verejnú prevádzku slúži **gunicorn** (zvláda viac požiadaviek, je rýchly a bezpečný). Na Renderi beží cez `Procfile` (máme z Etapy 3A).
- Overené, že nasadená appka je zdravá (`pocasie.onrender.com` homepage 200). Počasie stále čaká na koniec výpadku Open-Meteo (externé).

**Čo som dokázal:**
- **Projekt 7 dokončený** — appka je verejne na internete cez profesionálny postup (GitHub → Render → gunicorn). 🎉

**Kde sme skončili / ďalší krok:**
- Projekt 7 uzavretý. Ďalej podľa [VIBE-CODING-MAPA.md](VIBE-CODING-MAPA.md): F (GitHub/vetvy) / K (venv + debugging) / H (prepojené tabuľky), alebo pauza.

### Projekt 7 · Nasadenie — Etapa 3 (GitHub + Render) + ladenie nasadenia — 2026-06-11
**Čo sme prebrali:**
- Príprava na produkciu: **gunicorn** + **`Procfile`** (`web: gunicorn web_pocasie:app --bind 0.0.0.0:$PORT`).
- **GitHub**: vytvorený účet `silpet112` + repo `vibe-coding` (private), `git remote add` + `git push` (kód v cloude; `.env`/`*.db`/`bliss.jpg` ostali mimo vďaka `.gitignore`).
- **Render**: nasadenie z GitHubu (build `pip install -r requirements.txt`, start gunicorn). Appka **live**: `pocasie.onrender.com`.
- **Ladenie nasadenej appky**: keďže lokálne to nevidno, dočasne sme dali zobraziť detail chyby → zistili sme, že volanie počasia padá na **502 / SSL**. Overené z **3 sietí**: chyba je **výpadok servera Open-Meteo** (`api.open-meteo.com`), nie kód/sieť/Render (hľadanie miest funguje, ráno počasie šlo).

**Čo som dokázal:**
- Mám appku **verejne nasadenú na internete** (Etapa 3 cieľ splnený). Naučil som sa GitHub push aj ako sa ladí nasadená appka (logy/diagnostika). Commity `d09971c`, `b10a095` (+ GitHub `silpet112/vibe-coding`).

**Kde sme skončili / ďalší krok:**
- Počasie nabehne, keď sa Open-Meteo zotaví (kód aj nasadenie sú správne). Ďalej: Etapa 4 — uzavrieť Projekt 7.

### Projekt 7 · Nasadenie — Etapa 2 (tunel) — 2026-06-11
**Čo sme prebrali:**
- Pojem **tunel**: nástroj vytvorí dočasnú **verejnú URL** prepojenú s lokálnym serverom.
- Použili sme **cloudflared** (Cloudflare Tunnel) — **bez účtu** (jednoduchšie než ngrok); nainštalovaný cez winget.
- Spustili sme počasovú appku (port 5001) + `cloudflared tunnel --url http://localhost:5001` → verejná `*.trycloudflare.com` adresa. Overené zvonku (stav 200).

**Čo som dokázal:**
- Moja appka bola **dostupná na internete** cez verejný odkaz (funguje, kým beží PC + tunel). ✅

**Kde sme skončili / ďalší krok:**
- Etapa 3 — kód na **GitHub** + **trvalý hosting** (appka beží stále aj bez môjho PC). Pozn.: trycloudflare URL je dočasná a pri každom spustení nová.

### Projekt 7 · Nasadenie — Etapa 1 (requirements.txt) — 2026-06-09
**Čo sme prebrali:**
- Štart Projektu 7 (deployment); nasadzujeme počasovú appku `web_pocasie.py`.
- Pojem **`requirements.txt`** = zoznam balíčkov, ktoré si server podľa neho doinštaluje (`pip install -r requirements.txt`). Súvis s **venv** (izolovaný „batoh" balíčkov).
- Vytvorený `requirements.txt` (Flask, requests, python-dotenv), overený cez `pip install -r`.

**Čo som dokázal:**
- Appka má teraz „zoznam do batoha" pre akýkoľvek server. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 2 — tunel (ngrok): vlastná verejná URL k appke (budem si robiť účet na ngrok).

### Projekt 6 · Počasie cez API — Etapa 5 (testy) + UZAVRETÝ 🏁 — 2026-06-09
**Čo sme prebrali:**
- Testy **čistej logiky bez internetu** (`test_pocasie.py`, 14/14 PASS): `popis_pocasia`, `emoji_pocasia`, `nazov_dna`, `predpoved_z_dat` — poslednej sme podstrčili **vymyslené dáta** v tvare odpovede API.
- Prečo testy nezávisia od siete: oddelili sme „získať dáta z API" od „spracovať dáta" — testujeme to druhé.

**Čo som dokázal:**
- 14/14 PASS; commit `a7def26`. **Projekt 6 dokončený** — API, geocoding, web, 7-dňová predpoveď, emoji aj testy. 🎉

**Kde sme skončili / ďalší krok:**
- Projekt 6 uzavretý. Ďalej: Projekt 7 — **nasadenie** (sprístupniť appku na internete) alebo iná téma/pauza.

### Projekt 6 · Počasie cez API — Etapa 4 (web + predpoveď + emoji) — 2026-06-09
**Čo sme prebrali:**
- Počasie na **webe** cez Flask (`web_pocasie.py` + `templates/pocasie.html`), hero v štýle Windows XP lúky (CSS kresba; ak je `static/bliss.jpg`, zobrazí sa fotka). Web **znova použil** funkcie z `pocasie.py`.
- Iterácia: **7-dňová predpoveď** (Open-Meteo `daily`, `timezone=auto`), pomenovanie dní (`Dnes`/`Zajtra`/názov dňa + dátum) a **emoji** ku každému stavu (zrozumiteľné aj bez slovenčiny).
- Nové čisté funkcie: `emoji_pocasia`, `nazov_dna`, `predpoved_z_dat` (testovateľné).

**Čo som dokázal:**
- Zadám mesto na webe a vidím aktuálne počasie + 7-dňovú predpoveď s emoji; `bliss.jpg` lokálne funguje. Commit `07331aa`. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 5 — testy čistej logiky (popis/emoji/názvy dní/predpoveď) + uzavrieť Projekt 6.

### Projekt 6 · Počasie cez API — Etapa 3 (krajší výpis + chyby) — 2026-06-09
**Čo sme prebrali:**
- Krajší výpis: pocitová teplota + **slovný popis** (preklad `weather_code` cez slovník `POPISY_POCASIA`, čistá funkcia `popis_pocasia`).
- **Ošetrenie chýb**: `try/except requests.exceptions.RequestException` → pri výpadku internetu pekná hláška namiesto pádu.

**Čo som dokázal:**
- Appka vypíše teplotu/pocit/stav a pri simulovanom výpadku nespadla. Commit `2f2ff57`. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 4 (voliteľné: počasie na webe cez Flask) alebo Etapa 5 (testy + uzavrieť).

### Projekt 6 · Počasie cez API — Etapa 2 (mesto na vstupe) — 2026-06-09
**Čo sme prebrali:**
- **Reťazenie dvoch API volaní**: `najdi_mesto` (geocoding: názov → súradnice) → `stiahni_pocasie` (súradnice → teplota).
- Ošetrenie „mesto nenájdené" (`results` chýba → `None`); vstup mesta cez `input`.

**Čo som dokázal:**
- Zadám ľubovoľné mesto a appka mi vypíše jeho teplotu; vymyslené mesto pekne ohlási. Commit `7ad4e55`. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 3 — krajší výpis + ošetrenie chýb (žiadny internet, zlyhanie servera).

### Projekt 6 · Počasie cez API — Etapa 1 (prvé volanie) — 2026-06-09
**Čo sme prebrali:**
- Pojem **API** (čašník medzi programami), kolobeh **požiadavka → odpoveď**, a pojmy: endpoint/URL, parametre (query string), GET/POST, stavový kód (200/404), JSON, API kľúč. Mapa: [API-MAPA.md](API-MAPA.md).
- `pip install requests`; `pocasie.py`: `requests.get(...)` na Open-Meteo, `.json()` → slovník, vytiahnutie `data["current"]["temperature_2m"]`.
- Oddelená vrstva **`stiahni_pocasie`** (API) od **`teplota_z_dat`** (čistá logika) — testovateľné bez internetu.

**Čo som dokázal:**
- Spustil som appku a vrátila **živú teplotu z internetu**. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 2 — zadať ľubovoľné mesto → geocoding API zistí súradnice → počasie (dve volania za sebou).

### Bonus · Skill /app + povolenia + vypínacie tlačidlo — 2026-06-03
**Čo sme prebrali:**
- Vlastný skill **`/app`** (spustí Flask server na pozadí + otvorí prehliadač).
- **Allow-pravidlá** v `.claude/settings.local.json` (`Bash(python app.py)`, `PowerShell(Start-Process*)`), aby `/app` nepýtal povolenie — vopred povolené akcie.
- **Vypínacie tlačidlo 🛑** na webe (route `/vypni`, `os._exit` po odoslaní odpovede). Vysvetlené, prečo „auto-vypnutie pri zatvorení karty" nejde spoľahlivo (F5 vyzerá ako zatvorenie).

**Čo som dokázal:**
- Cez `/app` spúšťam a cez tlačidlo vypínam appku; commity `6838cc0`, `1c55ee9`. ✅

**Kde sme skončili / ďalší krok:**
- Projekty 1–5 hotové. Ďalej: Projekt 6 (väčšia výzva) alebo pauza.

### Projekt 5 · Rozšírenie webovej appky — Etapa 4 (testy) + UZAVRETÝ 🏁 — 2026-06-03
**Čo sme prebrali:**
- Ku každej novej funkcii pridať test. Rozšírený `test_vydavky.py` o testy mazania (`DELETE`), úpravy (`UPDATE`, `vydavok_podla_id`) a filtra (`vydavky_v_kategorii`) — na dočasnej DB v pamäti.
- Spolu **19/19 testov PASS**.

**Čo som dokázal:**
- Commit `82d4b23`. **Projekt 5 dokončený** — kompletný CRUD na webe, filter a testy. 🎉

**Kde sme skončili / ďalší krok:**
- Projekt 5 uzavretý. Ďalej: vybrať Projekt 6 (väčšia výzva) alebo pauza.

### Projekt 5 · Rozšírenie webovej appky — Etapa 3 (filtrovanie) — 2026-06-03
**Čo sme prebrali:**
- **Query string** = dodatočné info v adrese (`/?kategoria=jedlo`); vo Flasku sa číta cez `request.args.get(...)`.
- `databaza.vydavky_v_kategorii` (SQL `WHERE kategoria = ?`); odkazy na kategórie nad tabuľkou (`{{ kategoria|urlencode }}`), prehľad zostáva za všetko.
- Bonus: vytvorený skill **`/app`** — spustí server na pozadí a otvorí appku v prehliadači (commit `6838cc0`).

**Čo som dokázal:**
- Cez `/app` som si otvoril appku a vyskúšal filter podľa kategórie naživo. Commit `b502f63`. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 4 — testy nových funkcií (mazať/upraviť/filter) + uzavrieť Projekt 5.

### Projekt 5 · Rozšírenie webovej appky — Etapa 2 (úprava) — 2026-06-03
**Čo sme prebrali:**
- SQL **`UPDATE ... WHERE id = ?`** prepíše existujúci záznam. Tým máme **kompletný CRUD** (pridať/čítať/upraviť/zmazať).
- Úprava má 2 kroky: GET ukáže **predvyplnený** formulár (`templates/uprav.html`), POST uloží zmenu. Route `/uprav/<int:id>` slúži pre GET aj POST; `databaza.vydavok_podla_id` + `uprav_vydavok`.

**Čo som dokázal:**
- Upravil som výdavok z webu, formulár bol predvyplnený, zmena sa uložila. Commit `70ce688`. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 3 — filtrovanie zoznamu podľa kategórie (parametre v adrese / query string).

### Projekt 5 · Rozšírenie webovej appky — Etapa 1 (mazanie) — 2026-06-03
**Čo sme prebrali:**
- Štvrtá databázová operácia **`DELETE`** (vymazať riadok); spolu so `INSERT`/`SELECT`/`UPDATE` tvoria **CRUD** (Create, Read, Update, Delete).
- `databaza.zmaz_vydavok(conn, id)`, route `/zmaz/<int:id_vydavku>` (POST), v tabuľke tlačidlo 🗑️ s potvrdením (`onsubmit="return confirm(...)"`).

**Čo som dokázal:**
- Zmazal som výdavok z webu, potvrdenie funguje, súčty sa prepočítali. Commit `987dd01`. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 2 — úprava výdavku (predvyplnený edit formulár, SQL `UPDATE`).

### Projekt 4 · Výdavky na webe — Etapa 5 (vzhľad) + UZAVRETÝ 🏁 — 2026-06-03
**Čo sme prebrali:**
- Pojem **CSS**: HTML = *čo* je na stránke (obsah), CSS = *ako* to vyzerá (písmo, farby, rámčeky, odsadenie). Štýly pridané do `<head>` šablóny.
- Vyladený vzhľad: zelený nadpis, formulár v kartičke, prúžkovaná tabuľka, tlačidlo s efektom pri prejdení myšou.

**Čo som dokázal:**
- Appka funguje rovnako, ale vyzerá pekne. Commit `7d78966`. **Projekt 4 dokončený** — celá appka v prehliadači (stránka, šablóna, formulár, prehľady, CSS). 🎉

**Kde sme skončili / ďalší krok:**
- Projekt 4 uzavretý. Ďalej: vybrať Projekt 5 (väčšia výzva) alebo pauza.

### Projekt 4 · Výdavky na webe — Etapa 4 (prehľady na webe) — 2026-06-03
**Čo sme prebrali:**
- Prehľady na stránke: route `domov` zavolá `databaza.sucet_vsetkych` a `sucet_podla_kategorie`, výsledky pošle do šablóny.
- Žiadny nový databázový kód — len **znova použité** funkcie z Projektu 3 (odmena za upratanú architektúru).

**Čo som dokázal:**
- Na webe vidím súčet spolu aj rozpis podľa kategórie; po pridaní výdavku sa hneď prepočítajú. Commit `25e7930`. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 5 — vyladenie vzhľadu (trocha CSS) + uzavrieť Projekt 4.

### Projekt 4 · Výdavky na webe — Etapa 3 (formulár na webe) — 2026-06-03
**Čo sme prebrali:**
- Pojmy **GET** (daj mi stránku) vs **POST** (pošli serveru dáta z formulára). `<form method="post">` + `<input name="...">`.
- Nová route `/pridaj` (POST): prečíta `request.form`, sumu cez `logika.parsuj_sumu`, uloží cez `databaza.pridaj_vydavok`, potom **presmeruje** späť na `/` (aby F5 neodoslalo znova).

**Čo som dokázal:**
- Pridal som výdavok priamo z prehliadača cez formulár; neplatná suma sa bezpečne ignoruje. Commit `d04a2ff`. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 4 — prehľady na webe (súčty spolu/podľa kategórie; znova použiť `databaza.py`).

### Projekt 4 · Výdavky na webe — Etapa 2 (zoznam z DB na webe) — 2026-06-03
**Čo sme prebrali:**
- Pojem **HTML šablóna** (Jinja2): `{{ hodnota }}` vloží hodnotu, `{% for %}` opakuje (riadky tabuľky). Šablóny sú v priečinku `templates/`.
- `app.py` načíta výdavky cez `databaza.vsetky_vydavky()` a pošle ich do `templates/vydavky.html` cez `render_template`.

**Čo som dokázal:**
- Videl som svoje výdavky ako tabuľku v prehliadači — cez **tú istú `databaza.py`** ako terminál. Commit `a580c45`. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 3 — formulár na pridanie výdavku priamo na webe (odoslanie dát metódou POST).

### Projekt 4 · Výdavky na webe — Etapa 1 (prvá webová stránka) — 2026-06-03
**Čo sme prebrali:**
- Spustili sme Projekt 4 (cieľ: appka v prehliadači cez **Flask**; znova použijem vrstvy `databaza`/`logika`).
- Pojem **web server / route**: prehliadač pošle požiadavku na adresu (`http://127.0.0.1:5000`), server vráti stránku; `@app.route("/")` priradí funkciu k adrese.
- Nainštalovaný **Flask** (`pip install flask`), vytvorený `app.py` s jednou stránkou.

**Čo som dokázal:**
- Spustil som `python app.py` a videl vlastnú stránku v prehliadači. Server zastavím `Ctrl+C`. Commit `4b51a02`. ✅

**Kde sme skončili / ďalší krok:**
- Etapa 2 — zobraziť zoznam výdavkov z databázy priamo na webovej stránke (HTML šablóna).

### Projekt 3 · Správca výdavkov — Etapa E (testy) + UZAVRETÝ 🏁 — 2026-06-03
**Čo sme prebrali:**
- Testovací robot `test_vydavky.py` (11 testov) pre vrstvy `logika` a `databaza`; beží na **dočasnej DB v pamäti** (`:memory:`), takže sa nedotkne reálnych dát.
- Test najprv odhalil **zlý predpoklad v samotnom teste** (poradie je podľa dátumu, nie podľa pridania) — opravený na kontrolu nezávislú od poradia. Pekná ukážka, načo testy sú.

**Čo som dokázal:**
- 11/11 PASS; commit `afe3fe2`. **Projekt 3 dokončený** — databáza, .env, architektúra, prehľady aj testy. 🎉

**Kde sme skončili / ďalší krok:**
- Projekt 3 uzavretý. Ďalej: vybrať Projekt 4 (väčšia výzva) alebo pauza.

### Projekt 3 · Správca výdavkov — Etapa D (prehľady cez dotazy) — 2026-06-03
**Čo sme prebrali:**
- Databáza vie aj **počítať**: `SUM(suma)` = súčet, `GROUP BY kategoria` = zoskup a spočítaj po kategóriách, `WHERE datum LIKE '2026-06%'` = filter za mesiac.
- Pridané do `databaza.py`: `sucet_vsetkych`, `sucet_podla_kategorie`, `sucet_za_mesiac`; do menu prehľady 3/4/5.

**Čo som dokázal:**
- Overil som súčty na ručnom príklade (spolu 22, jedlo 10/doprava 12, jún 10/máj 12) — sedí. Commit `eddd002`. ✅

**Kde sme skončili / ďalší krok:**
- Etapa E — automatické testy (na dočasnej DB) + uzavrieť Projekt 3.

### Projekt 3 · Správca výdavkov — Etapa C (architektúra) — 2026-06-03
**Čo sme prebrali:**
- Pojem **architektúra** = rozdelenie appky na **vrstvy**, každá s jednou zodpovednosťou (prirovnanie reštaurácia: sklad/kuchyňa/čašník/pravidlá).
- Refaktor `vydavky.py` na 4 súbory: `konfig.py` (nastavenia/.env), `databaza.py` (SQL), `logika.py` (čisté výpočty), `vydavky.py` (menu/obsluha).
- Appka robí **to isté**, ale je prehľadná a vrstvy `databaza`/`logika` sa dajú samostatne testovať (využijeme v Etape E).

**Čo som dokázal:**
- Overil som, že appka po rozdelení funguje rovnako (pridať/zobraziť, dáta prežijú). Commit `d03ba67`. ✅

**Kde sme skončili / ďalší krok:**
- Etapa D — **prehľady cez dotazy**: súčet všetkých výdavkov, súčet podľa kategórie, za mesiac (SQL `SUM`/`GROUP BY`).

### Projekt 3 · Správca výdavkov — Etapa B (.env) — 2026-06-03
**Čo sme prebrali:**
- Pojem **.env**: nastavenia/tajomstvá **mimo kódu** v tvare `KLÚČ=hodnota`; `.env` patrí do `.gitignore` (nesmie do gitu), do gitu ide len vzor **`.env.example`**.
- Prvý **`pip install`** (`python-dotenv`) — doinštalovanie hotového balíčka.
- Upravili sme `vydavky.py`: `DB_SUBOR` a `MENA` sa načítajú z `.env` cez `load_dotenv()` + `os.getenv()`.

**Čo som dokázal:**
- Overil som naživo, že zmena `MENA` v `.env` zmení výpis appky **bez zásahu do kódu**. Commit `ef12072`. ✅
- Potvrdil som, že git `.env` ignoruje (`git check-ignore`), `.env.example` verzuje.

**Kde sme skončili / ďalší krok:**
- Etapa C — **architektúra**: rozdeliť appku na vrstvy (`databaza.py` / `logika.py` / `konfig.py` / `vydavky.py`).

### Projekt 3 · Správca výdavkov — Etapa A (MVP s databázou) — 2026-06-03
**Čo sme prebrali:**
- Spustili sme Projekt 3 (cieľ: naučiť sa **architektúru, .env, databázu** — postupne po etapách A–E).
- Pojem **databáza**: ako excelovská tabuľka s riadkami/stĺpcami, ktorú ovládaš príkazmi SQL (`INSERT` pridaj, `SELECT` vyber). Použili sme **SQLite** — vstavanú v Pythone, celá v jednom súbore `vydavky.db`.
- Postavili sme MVP `vydavky.py`: pridať výdavok (suma, kategória, dátum, poznámka) a zobraziť všetky.

**Čo som dokázal:**
- Overil som kľúčovú vec: dáta **prežijú zatvorenie programu** (sú v databáze, nie v pamäti). Commit `d2f3f97`. ✅
- Pridal som `*.db` do `.gitignore` (dáta sa neverzionujú — rovnaký návyk ako `ulohy.json`).

**Kde sme skončili / ďalší krok:**
- Etapa B — **.env**: nastavenia (názov DB, mena) mimo kódu; `.env.example` + gitignore; prvý `pip install`.

### Projekt 2 · Kalkulačka — automatické testy — 2026-06-03
**Čo sme prebrali:**
- Pridaný „testovací robot" `test_kalkulacka.py` — 14 testov pre všetky funkcie (sčítať, odčítať, násobiť, deliť, delenie nulou, parsovanie čísla, chaining). Spustenie: `python test_kalkulacka.py`.
- Robot sa dá spustiť po **každej úprave** kódu a hneď povie PASS/FAIL — strážca, že sa nič nepokazilo.

**Čo som dokázal:**
- Mám automatickú kontrolu pri oboch projektoch (todo aj kalkulačka). Commit `e9b6f9e`. ✅

**Kde sme skončili / ďalší krok:**
- Kalkulačka je hotová a otestovaná. Ďalej: ďalšie vylepšenie alebo uzavrieť Projekt 2.

### Projekt 2 · Kalkulačka — iterácie — 2026-06-03
**Čo sme prebrali:**
- Dve iterácie (viedol som sám): (1) výsledok operácie sa stáva základom pre ďalšiu (chaining), (2) pridané násobenie a delenie + ošetrené delenie nulou. Overené na príkladoch (5×8=40, 8÷2=4); commity `cc24b95`, `ab427b5`.

**Čo som dokázal:**
- Zadal som vylepšenia, overil výsledky a commitol — režisérsky cyklus v praxi. ✅

**Kde sme skončili / ďalší krok:**
- Kalkulačka má 4 operácie + chaining. Ďalej: testy / ďalšie vylepšenie / uzavrieť Projekt 2.

### Projekt 2 · Kalkulačka — MVP (viedol som sám) — 2026-06-03
**Čo sme prebrali:**
- Samostatne som aplikoval recept: vízia + MVP (sčítanie/odčítanie) + plán (menu pridať/sčítať/odčítať/koniec) + príklady. Claude postavil `kalkulacka.py` (oddelená logika), overené na príkladoch (2+7=9, 8−6=2), commit `1fb7e7c`.

**Čo som dokázal:**
- Viedol som projekt takmer sám — zadanie, kontrola výsledku, commit. ✅

**Praktická úloha:**
- Navrhnúť MVP a doviesť kalkulačku k fungujúcej overenej verzii — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Iterovať (násobenie/delenie…) alebo uzavrieť Projekt 2.

### Bonus — Automatické testy — 2026-06-03
**Čo sme prebrali:**
- Čo je automatický test (samostatný program, čo sám overí logiku appky). Refaktor `todo.py` (oddelená čistá logika od obsluhy) → `test_todo.py` s 9 testami; spustenie `python test_todo.py`.

**Čo som dokázal:**
- 9/9 testov PASS; chápem, že testy chytia chybu (napr. tú z Etapy 5) automaticky. Commit `75f59fb`. ✅

**Praktická úloha:**
- Nechať si vytvoriť a spustiť automatické testy — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Nový projekt / ďalšie vylepšenie todo / iná téma.

### Stavanie s AI · Etapa 7 — Zhrnutie (recept) — 2026-06-03  🎉 PROJEKT 1 HOTOVÝ
**Čo sme prebrali:**
- Zhrnutie režisérskeho cyklu (Vízia → MVP → Plán → Postav → Over → Commit → Iteruj → uzavri) ako opakovateľný recept; prešli sme, ako som ho použil na Správcovi úloh.

**Čo som dokázal:**
- Postavil som s AI celý prvý projekt (Správca úloh, 5 commitov) a viem recept zopakovať. ✅

**Praktická úloha:**
- Pochopiť a vedieť zopakovať režisérsky cyklus — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Cesta „Stavanie s AI" (Etapy 1–7) dokončená. Ďalej: nový projekt podľa receptu, alebo iná téma.

### Stavanie s AI · Etapa 6 — Vyladenie (priorita) — 2026-06-03
**Čo sme prebrali:**
- Pridané vyladenie: priorita úlohy + bledozelený text v termináli (ANSI farby, `os.system("")` na Windows, `*` ako poistka). Disciplína „kedy je hotovo" (vyhnúť sa feature-creep).

**Čo som dokázal:**
- Zadal som rozšírenie (priorita + farba), overil a commitol `3039e39`. Projekt vyhlásený za hotový. ✅

**Praktická úloha:**
- Pridať jedno vyladenie a uzavrieť projekt — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Ďalej Etapa 7 — zhrnutie, recept na ďalší projekt.

### Stavanie s AI · Etapa 5 — Riadený debugging — 2026-06-03
**Čo sme prebrali:**
- Chyby sú normálne; dobrý popis = čo som čakal / čo sa stalo / ako zopakovať; záchranné siete = commit + `/rewind`. Bonus otázka: čo je `/compact` a čo pri ~100% kontextu.

**Čo som dokázal:**
- Našiel som chybu pri používaní (hotová úloha sa nezaškrtla), jasne ju opísal, Claude opravil, ja overil. ✅ (Chyba bola nácviková; reálne zastaví overovanie + neskôr testy.)

**Praktická úloha:**
- Nájsť, opísať a dať opraviť chybu — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Ďalej Etapa 6 — vyladenie + „kedy je hotovo". (Možná budúca téma: automatické testy.)

### Stavanie s AI · Etapa 4 — Iterácia (mazanie úloh) — 2026-06-03
**Čo sme prebrali:**
- Iteračný cyklus: použiť → všimnúť si → konkrétne zadať → postaviť → overiť → commit. Pridaná funkcia mazania úloh s potvrdením (a/n) pred zmazaním.

**Čo som dokázal (ako režisér):**
- Konkrétne som zadal vylepšenie (mazanie + potvrdenie), overil obe cesty (n nezmaže, a zmaže) a uložil commit `0615bab`. ✅

**Praktická úloha:**
- Vybrať a doriadiť jednu iteráciu — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Ďalej Etapa 5 — riadený debugging (keď sa niečo pokazí).

### Stavanie s AI · Etapa 3 — Postav MVP + over + commit — 2026-06-03
**Čo sme prebrali:**
- Claude postavil MVP (`todo.py`); ja som appku **sám spustil a overil** (funguje); pridali sme poistku (bezpečné načítanie súboru); commit.

**Čo som dokázal:**
- Prvá appka postavená s AI **funguje**! Uložená commitom `974cdda`. Bonus: rozlíšil som test-artefakt (PowerShell pomotal nasimulovaný vstup) od skutočnej chyby kódu. ✅

**Praktická úloha:**
- Spustiť a overiť appku + uložiť commit — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Ďalej Etapa 4 — iterácia (vylepšenia podľa používania).

### Stavanie s AI · Etapa 2 — Plán pred stavbou — 2026-06-03
**Čo sme prebrali:**
- Plán stavby pred kódením (`todo.py`, menu 1–4, ukladanie do súboru); schválil som ho ako režisér.

**Praktická úloha:**
- Schváliť plán stavby — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Etapa 3 — postaviť MVP.

### Stavanie s AI · Etapa 1 — Vízia → MVP — 2026-06-03
**Čo sme prebrali:**
- Režisérska rola (ja vediem, Claude stavia); vízia (1 veta) vs. MVP (najmenšia užitočná verzia); prečo začať v malom.

**Čo som rozhodol (ako režisér):**
- MVP Správcu úloh = pridať / zobraziť / označiť hotovú / uložiť. Rozšírenia až neskôr. ✅

**Praktická úloha:**
- Schváliť rozsah MVP — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Ďalej Etapa 2 — plán, ako MVP postaviť.

### Lekcia E20 — Súhrn najlepších návykov — 2026-06-02  🎓 CELÝ KURZ DOKONČENÝ!
**Čo sme prebrali:**
- 5 návykov: spravuj kontext, vždy over, najprv plán, buď konkrétny, oprav skoro; bonus writer/reviewer.

**Čo som pochopil:**
- Najviac mi sadol návyk č. 2 — vždy si dať overenie (rozdiel medzi „vyzerá hotovo" a „je hotovo"). ✅

**Praktická úloha:**
- Reflexia: vybrať návyk s najväčším zmyslom — zvládnuté (overovanie).

**Kde sme skončili / ďalší krok:**
- 🎉 Dokončený CELÝ kurz Claude Code (A1–E20). Ďalej: prax, faktoriál v Pythone, alebo programovacia osnova.

### Lekcia E19 — Plánovanie a automatizácia — 2026-06-02
**Čo sme prebrali:**
- `/loop` (opakovanie počas sedenia), naplánované úlohy/routines (cloud, bežia aj bez PC), pripomienky.

**Čo som pochopil:**
- Na úlohu „každé ráno aj pri vypnutom PC" = routine (beží sama na serveri); `/loop` potrebuje otvorené sedenie. ✅

**Praktická úloha:**
- Vybrať správny nástroj (routine vs. `/loop`) — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Ďalej E20 — posledná lekcia, súhrn najlepších návykov.

### Lekcia E18 — Workflowy a multi-agent orchestrácia — 2026-06-02
**Čo sme prebrali:**
- Workflow = riadenie veľa agentov podľa skriptu; na veľké úlohy (migrácie, audity, research); spustenie slovami + `/workflows`. Rozdiel subagent (1) vs. workflow (tím).

**Čo som pochopil:**
- Workflow sa hodí na veľké/opakované úlohy (napr. 200 súborov), nie na drobnosť ako jeden preklep. ✅

**Praktická úloha:**
- Rozpoznať, kedy použiť workflow (b: 200 súborov) — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Ďalej E19 (Plánovanie a automatizácia).

### Lekcia D17 — Hooks — 2026-06-02  ✅ Modul D dokončený
**Čo sme prebrali:**
- Hook = príkaz spustený automaticky/deterministicky pri udalosti (PostToolUse, SessionStart…); rozdiel oproti CLAUDE.md (odporúčanie vs. istota); nastavenie v `settings.json`.

**Čo som pochopil:**
- CLAUDE.md = odporúčania; hook = vynútené pravidlo, ktoré program spustí vždy (nezávisí od „rozhodnutia" Claude). ✅

**Praktická úloha:**
- Vysvetliť rozdiel CLAUDE.md vs. hook — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Hotový celý Modul D. Ďalej Modul E, Lekcia E18 (Workflowy).

### Lekcia D16 — MCP servery — 2026-06-02
**Čo sme prebrali:**
- MCP = pripojenie externých služieb (Gmail, Kalendár, Drive, Notion, ClickUp…); Claude s nimi vie pracovať; pridanie cez `claude mcp add` / konektory.

**Čo som pochopil:**
- Mám viacero MCP nástrojov pripojených; Claude do osobných dát siaha len na požiadanie. ✅ (Bonus: skilly `/pod`, `/pokracuj` po reštarte fungujú.)

**Praktická úloha:**
- Pochopiť princíp MCP + že mám reálne pripojené nástroje — zvládnuté (živú ukážku sme nechali na neskôr).

**Kde sme skončili / ďalší krok:**
- Ďalej D17 (Hooks) — posledná lekcia Modulu D.

### Lekcia D15 — Subagenty — 2026-06-02
**Čo sme prebrali:**
- Subagent = delegovaný Claude vo vlastnej pamäti (vráti zhrnutie); typy Explore/Plan/general-purpose; vlastné v `.claude/agents/`; paralelný beh.

**Čo som pochopil:**
- Naživo: Explore agent prečítal 544-riadkovú MAPU a vrátil len krátke zhrnutie modulov — môj kontext ostal čistý. ✅ (Pozn.: aj agent sa môže drobne pomýliť — preto výsledky prečítaj.)

**Praktická úloha:**
- Sledovať subagenta pri reálnej úlohe — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Ďalej D16 (MCP servery).

### Lekcia D14 — Skills a vlastné slash príkazy — 2026-06-02
**Čo sme prebrali:**
- Čo je skill (vlastný príkaz), kde žije (`.claude/skills/názov/SKILL.md`), frontmatter + telo, load-on-demand. Už použité skilly: `/init`, `/update-config`.

**Čo som pochopil:**
- Vytvorili sme vlastný skill `/pokracuj`, ktorý prečíta POKROK.md a pokračuje v kurze. ✅

**Praktická úloha:**
- Vyrobiť vlastný skill + skontrolovať, či sa objaví v zozname (`/`). (Nový skill sa občas objaví až po reštarte.)

**Kde sme skončili / ďalší krok:**
- Ďalej D15 (Subagenty).

### Lekcia D13 — settings.json a povolenia — 2026-06-02
**Čo sme prebrali:**
- `settings.json` za `/config`; permissions allow/deny/ask, defaultMode, model, env; 3 umiestnenia (user/projekt/local); wildcardy v allow-rule.

**Čo som pochopil:**
- Pozreli sme môj reálny `.claude/settings.local.json` — má allow-rule s presným príkazom, ktorý som predtým schválil „always allow". ✅

**Praktická úloha:**
- Prečítať a pochopiť vlastný `settings.local.json` — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Ďalej D14 (Skills a vlastné slash príkazy).

### Lekcia C12 — Git a verzie — 2026-06-02  ✅ Modul C (jadro)
**Čo sme prebrali:**
- Git: história verzií, commit (= uložená verzia s popisom), repo, diff, vetva; ako ho Claude používa; `/review`, `/code-review`. Rozdiel oproti rewind (trvalé vs. rýchle späť).

**Čo som pochopil:**
- Rozumiem, načo je git a commit. Explore ukázal, že git nie je nainštalovaný → praktický commit odložený. ✅ (koncepty)

**Praktická úloha:**
- Doinštalovali sme Git (winget, v2.54) a spravili **prvý reálny commit** (`554c82a`, 5 súborov, 926 riadkov) — hotové! ✅

**Kde sme skončili / ďalší krok:**
- Hotové jadro kurzu (A–C) + prvý commit. Repo je založené. Ďalej Modul D (pokročilé) — alebo doinštalovať Python.

### Lekcia C11 — Claude Code vo VS Code — 2026-06-02
**Čo sme prebrali:**
- VS Code špecifiká: panel, inline diffy, výber textu = kontext, @-odkazy s riadkami, skratky. Naživo „výber = kontext".

**Čo som pochopil:**
- Označil som funkciu `Faktorial` a Claude ju videl bez kopírovania; prešli sme, čo kód robí (function, param, if, for, return) + príklad 4! = 24. ✅

**Praktická úloha:**
- Označiť riadky a opýtať sa „čo robia tieto riadky" — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Ďalej C12 (Git a verzie).

### Lekcia B10 — Správa sedení — 2026-06-02  ✅ Modul B dokončený
**Čo sme prebrali:**
- Sedenia sa ukladajú; `/resume`, `/clear`, `/rename`, `--continue`; jedna téma = jedno sedenie (anti-pattern „kuchynský drez").

**Čo som pochopil:**
- Rozumiem správe sedení. Bonus: `/rename` v tomto prostredí nie je dostupný — nie každý príkaz je všade (CLI vs VS Code). Na pokračovanie mi stačí otvoriť priečinok a povedať „pokračujme". ✅

**Praktická úloha:**
- Skúsiť `/rename` — v tomto prostredí nedostupné; pochopený rozdiel CLI vs prostredie.

**Kde sme skončili / ďalší krok:**
- Hotový Modul B (B5–B10) → **polovica kurzu!** Ďalej Modul C, Lekcia C11 (VS Code).

### Lekcia B9 — Vrátenie zmien a bezpečné experimentovanie — 2026-06-02
**Čo sme prebrali:**
- Checkpointy (snímky pri každom prompte), `/rewind` a Esc Esc, voľba vrátiť kód/rozhovor; mentalita bezfstrachového experimentu.

**Čo som pochopil:**
- Sám som cez /rewind vrátil experimentálnu zmenu (`$cislo` 20 → 6). Tabuľka promptov = zoznam snímok. ✅

**Praktická úloha:**
- Vrátiť experimentálnu zmenu v `faktorial.ps1` cez rewind — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Ďalej B10 (Správa sedení) — posledná lekcia Modulu B.

### Lekcia B8 — Plánovací režim + prvý program — 2026-06-02
**Čo sme prebrali:**
- Postup explore → plan → code → over. Naživo: zistili sme, že Python nie je nainštalovaný, zvolili PowerShell, naplánovali a schválili plán, napísali `faktorial.ps1` a overili ho.

**Čo som pochopil:**
- Pri väčšej úlohe sa oplatí najprv plán; vlastné testy dávajú istotu. Môj prvý program funguje (6! = 720, všetky kontroly OK). ✅

**Praktická úloha:**
- Naplánovať a postaviť program na faktoriál + nechať ho samého sa overiť — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Vznikol `faktorial.ps1` (mením premennú `$cislo`). Ďalej B9 (Vrátenie zmien / rewind).

### Lekcia B7 — Ako dobre zadávať úlohy (prompting) — 2026-06-02
**Čo sme prebrali:**
- 4 pravidlá promptingu: konkrétnosť, príklad, žiadosť o overenie, iterovanie; mentalita delegovania kolegovi.

**Čo som pochopil:**
- Sám som napísal dobrý prompt (faktoriál + overenie) — použil pravidlá 1 a 3; doplniť sa dal príklad (pravidlo 2). ✅

**Praktická úloha:**
- Prepísať vágne zadanie na konkrétne — zvládnuté (vlastný prompt na výpočet faktoriálu).

**Kde sme skončili / ďalší krok:**
- Ďalej B8 (Plánovací režim) — alebo bonus: naozaj spustiť faktoriál ako prvý program.

### Lekcia B6 — CLAUDE.md (pamäť projektu) — 2026-06-02
**Čo sme prebrali:**
- Čo je CLAUDE.md (číta sa na začiatku každého sedenia), kam patrí, čo doň (ne)písať, držať krátko; `/init`.

**Čo som pochopil:**
- Cez `/init` som vytvoril prvý CLAUDE.md — videl som čítanie priečinka, diff aj povolenie. ✅

**Praktická úloha:**
- Spustiť `/init` a schváliť vytvorenie CLAUDE.md — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Ďalej Lekcia B7 (Ako dobre zadávať úlohy).

### Lekcia B5 — Slash príkazy denne — 2026-06-02
**Čo sme prebrali:**
- Čo sú slash príkazy a prehľad denných; do hĺbky `/model` (Opus/Sonnet/Haiku) a `/config` (nastavenia). Bonus: `/update-config` ako príklad skillu meniaceho settings.json.

**Čo som pochopil:**
- `/` ukáže zoznam; `/model` prepne model podľa potreby; `/config` = klikacie nastavenia. ✅

**Praktická úloha:**
- Spustiť `/help`, vybrať príkazy (`/model`, `/config`) a nechať si ich vysvetliť — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Ďalej Lekcia B6 — vytvoríme prvý CLAUDE.md.

### Lekcia A4 — Súbory a kontext — 2026-06-02  ✅ Modul A dokončený
**Čo sme prebrali:**
- Čítanie súborov (žiadosť alebo @-odkaz); čo je kontext (pamäť rozhovoru, obmedzená, v tokenoch); `/context` (využitie) a `/clear` (vyčistenie medzi témami) + varovanie nespúšťať teraz.

**Čo som pochopil:**
- `/context` mi ukázal tabuľku tokenov — na čo sa minuli a koľko zostáva. Token = malý kúsok textu. ✅

**Praktická úloha:**
- Spustiť `/context` a opísať tabuľku; vyskúšať `@` zoznam súborov — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Hotový celý Modul A (A1–A4). Ďalej Modul B, Lekcia B5 (Slash príkazy denne).

### Lekcia A3 — Povolenia a režimy — 2026-06-02
**Čo sme prebrali:**
- Prečo Claude pýta povolenie; režimy: ask before edits (Default) / edit automatically / plan / auto; prepínanie Shift+Tab; bezpečné návyky.

**Čo som pochopil:**
- Prepol som cez Shift+Tab a videl všetky 4 režimy; na štart ostávam v „ask before edits" (Default). ✅

**Praktická úloha:**
- Vyskúšať Shift+Tab, vymenovať režimy a vrátiť sa na Default — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Pokračujeme Lekciou A4 (Súbory a kontext) — posledná v Module A.

### Lekcia A2 — Prvý rozhovor a rozhranie — 2026-06-02
**Čo sme prebrali:**
- Turn (kolo), tool use (viditeľný krok „Read…"), diff (🟩/🟥), Esc a Shift+Enter.

**Čo som pochopil:**
- Keď Claude číta súbory, zobrazí sa krok „Read…" — to je „získa kontext" naživo. ✅

**Praktická úloha:**
- Opýtať sa na obsah POKROK.md a všimnúť si krok „Read POKROK.md" — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Pokračujeme Lekciou A3 (Povolenia a režimy).

### Lekcia A1 — Čo je Claude Code a ako „rozmýšľa" — 2026-06-02
**Čo sme prebrali:**
- Rozdiel agent vs. chatbot; agentický cyklus (získa kontext → koná → overí); kde Claude Code beží; Esc ako brzda.

**Čo som pochopil:**
- Claude Code vykonáva zadané úlohy a ja ho usmerňujem a kontrolujem; chatbot iba vysvetľuje a odpovedá. ✅

**Praktická úloha:**
- Vlastnými slovami vysvetliť rozdiel agent vs. chatbot — zvládnuté.

**Kde sme skončili / ďalší krok:**
- Pokračujeme Lekciou A2 (Prvý rozhovor a rozhranie) — agentický cyklus naživo.

<!--
### Lekcia X — [Názov témy] — [dátum]
**Čo sme prebrali:**
- ...

**Čo som pochopil:**
- ...

**Praktická úloha:**
- ...

**Kde sme skončili / ďalší krok:**
- ...
-->

---

## Moja osnova (prehľad celej cesty)
*(Zaškrtáva sa, ako postupujem. Poradie sa môže meniť podľa potreby.)*

- [ ] 1. Ako program a počítač „rozmýšľajú"
- [ ] 2. Úplné základy (premenné, dátové typy, podmienky, cykly, funkcie)
- [ ] 3. Dátové štruktúry
- [ ] 4. Ako čítať a chápať kód
- [ ] 5. Štruktúra projektu a logické myslenie
- [ ] 6. Práca s nástrojmi (VS Code + Claude Code)
- [ ] 7. Frontend vs. backend, web vs. aplikácia (API, databáza)
- [ ] 8. Debugging
- [ ] 9. Git a verzionovanie
- [ ] 10. Bezpečnosť a dobré návyky

---

## Claude Code — osnova (samostatná cesta) 🗺️
*(Samostatná cesta na ovládnutie nástroja Claude Code — oddelená od programovacej osnovy
vyššie. Detailná referencia ku každej lekcii je v [CLAUDE-CODE-MAPA.md](CLAUDE-CODE-MAPA.md).)*

**Ako to funguje:**
- 1 lekcia ≈ jedno krátke sedenie; tempo upravíme podľa teba.
- Každá lekcia: krátko vysvetlím → spolu naživo vyskúšame → dostaneš malú úlohu →
  zapíšem pokrok sem do POKROK.md (Denník lekcií + zaškrtnem bod nižšie).
- Značky: 🟢 základ · 🔵 mierne pokročilé · 🟣 neskôr / pre pokročilých.

**MODUL A — Základy a prvé kroky** 🟢
- [x] A1. Čo je Claude Code a ako „rozmýšľa" (agentický cyklus; kde beží)
- [x] A2. Prvý rozhovor a rozhranie (turn, tool use, Esc)
- [x] A3. Povolenia a režimy (Default / accept-edits / Plan, Shift+Tab)
- [x] A4. Súbory a kontext (@-odkazy, `/context`, `/clear`)

**MODUL B — Každodenná práca** 🟢🔵
- [x] B5. Slash príkazy denne (`/help`, `/clear`, `/init`, `/model`, `/review`…)
- [x] B6. CLAUDE.md — pamäť projektu (`/init`)
- [x] B7. Ako dobre zadávať úlohy (prompting)
- [x] B8. Plánovací režim do hĺbky (preskúmaj → naplánuj → koduj)
- [x] B9. Vrátenie zmien a bezpečné experimentovanie (`/rewind`)
- [x] B10. Správa sedení (resume, rename, clear)

**MODUL C — VS Code + Git** 🔵
- [x] C11. Claude Code vo VS Code (panel, diffy, @-odkazy, skratky)
- [x] C12. Git základ a ako ho Claude používa (`/review`, `/code-review`) — koncepty ✅ + Git nainštalovaný a prvý commit hotový ✅

**MODUL D — Prispôsobenie a rozšírenie** 🟣
- [x] D13. settings.json a povolenia do hĺbky
- [x] D14. Skills a vlastné slash príkazy
- [x] D15. Subagenty (Agent)
- [x] D16. MCP servery (externé nástroje)
- [x] D17. Hooks (automatizácia pravidiel)

**MODUL E — Automatizácia a škálovanie** 🟣
- [x] E18. Workflowy a multi-agent orchestrácia
- [x] E19. Plánovanie a automatizácia (`/loop`, routines)
- [x] E20. Súhrn najlepších návykov  🎓

---

## Stavanie s AI — Projekt 1: Správca úloh (to-do) 🏗️
*(Deň 2+. Cieľ: naučiť sa stavať projekty s AI — ja režisér, Claude staviteľ. Playbook:
[STAVANIE-S-AI.md](STAVANIE-S-AI.md). Formát: krátke sedenia, hands-on, logované sem.)*

**Režisérsky cyklus:** Vízia → MVP → Plán → Postav → Spusti & over → Commit → Iteruj.

- [x] Etapa 1 — Vízia → MVP (zadefinovať, čo appka robí; najmenšia užitočná verzia)
- [x] Etapa 2 — Plán pred stavbou (Claude navrhne, ja schválim)
- [x] Etapa 3 — Postav MVP + spusti + over + commit
- [x] Etapa 4 — Iterácia podľa používania (spätná väzba, vylepšenia)
- [x] Etapa 5 — Keď sa niečo pokazí (riadený debugging)
- [x] Etapa 6 — Vyladenie + „kedy je hotovo"
- [x] Etapa 7 — Zhrnutie (recept na ďalší projekt)  🎉

---

## Stavanie s AI — Projekt 2: Kalkulačka 🧮
*(Deň 2+. Cieľ: upevniť recept, používateľ vedie viac sám. Recept: Vízia → MVP → Plán →
Postav → Over → Commit → Iteruj → uzavri.)*

- [x] Vízia → MVP (definuje používateľ) — sčítanie + odčítanie
- [x] Plán + postaviť MVP + spustiť & overiť + commit — `kalkulacka.py`, commit `1fb7e7c`
- [x] Iterácie — chaining výsledku + násobenie/delenie (commit `ab427b5`); testy voliteľné
- [x] Automatické testy — `test_kalkulacka.py` (14 testov, PASS), commit `e9b6f9e`
- [ ] Uzavrieť projekt

---

## Stavanie s AI — Projekt 3: Správca výdavkov 💰
*(Deň 3+. Cieľ: väčší reálny projekt + naučiť sa **architektúru, .env, databázu** — postupne, jeden
pojem na etapu. Téma: zapisovanie výdavkov a prehľady. Stále ten istý režisérsky recept.)*

- [x] **Etapa A** — Vízia → MVP s databázou (SQLite): pridať/zobraziť výdavok, dáta v `vydavky.db`. Commit `d2f3f97`
- [x] **Etapa B** — `.env` (nastavenia mimo kódu: `DB_SUBOR`, `MENA`; `.env.example` + gitignore; `pip install python-dotenv`). Commit `ef12072`
- [x] **Etapa C** — Architektúra (rozdelenie na vrstvy: `konfig.py` / `databaza.py` / `logika.py` / `vydavky.py`). Commit `d03ba67`
- [x] **Etapa D** — Prehľady cez dotazy (súčet spolu, podľa kategórie, za mesiac; SQL `SUM`/`GROUP BY`). Commit `eddd002`
- [x] **Etapa E** — Automatické testy (`test_vydavky.py`, 11 testov, DB v pamäti). Commit `afe3fe2`
- [x] **Projekt 3 UZAVRETÝ** 🏁 — databáza · .env · architektúra · prehľady · testy

---

## Stavanie s AI — Projekt 4: Výdavky na webe 🌐
*(Cieľ: vykročiť z terminálu do prehliadača cez **Flask**; znova použiť vrstvy `databaza.py` a
`logika.py` z Projektu 3 — len obsluhu vymeníme za web. Ukáže silu vrstvenej architektúry.)*

- [x] **Etapa 1** — Prvá webová stránka (Flask, route `/`, `python app.py` → `http://127.0.0.1:5000`). Commit `4b51a02`
- [x] **Etapa 2** — Zobraziť zoznam výdavkov z databázy na stránke (HTML šablóna). Commit `a580c45`
- [x] **Etapa 3** — Formulár na pridanie výdavku (POST + presmerovanie). Commit `d04a2ff`
- [x] **Etapa 4** — Prehľady na webe (súčet spolu + podľa kategórie; znova použité `databaza.py`). Commit `25e7930`
- [x] **Etapa 5** — Vyladenie vzhľadu (CSS v šablóne). Commit `7d78966`
- [x] **Projekt 4 UZAVRETÝ** 🏁 — Flask web: stránka · šablóna · formulár (POST) · prehľady · CSS

---

## Stavanie s AI — Projekt 5: Rozšírenie webovej appky 🛠️
*(Cieľ: stavať na existujúcej appke — pridať CRUD operácie, ktoré chýbali. Učím sa rozširovať
hotový projekt bez prepisovania od nuly.)*

- [x] **Etapa 1** — Mazanie výdavku (SQL `DELETE`, tlačidlo s potvrdením). Commit `987dd01`
- [x] **Etapa 2** — Úprava výdavku (predvyplnený edit formulár, SQL `UPDATE`; kompletný CRUD). Commit `70ce688`
- [x] **Etapa 3** — Filtrovanie podľa kategórie (query string `?kategoria=...`). Commit `b502f63`
- [x] **Etapa 4** — Testy nových funkcií (`test_vydavky.py`, 19/19 PASS). Commit `82d4b23`
- [x] **Projekt 5 UZAVRETÝ** 🏁 — kompletný CRUD na webe · filter · testy

---

## Stavanie s AI — Projekt 6: Počasie cez API 🌦️
*(Cieľ: naučiť sa, čo je **API** a ako appka ťahá dáta z internetu. Téma: počasie cez Open-Meteo
— zadarmo, bez kľúča. Mapa pojmov: [API-MAPA.md](API-MAPA.md).)*

- [x] **Etapa 1** — Pochopiť API + prvé volanie (Open-Meteo, `pip install requests`, vypísať teplotu)
- [x] **Etapa 2** — Mesto na vstupe → súradnice (geocoding API) → počasie (dve volania za sebou). Commit `7ad4e55`
- [x] **Etapa 3** — Pekný výpis (pocitová teplota + popis) + ošetrenie chýb. Commit `2f2ff57`
- [x] **Etapa 4** — Počasie na webe (Flask, hero v štýle XP) + 7-dňová predpoveď s emoji. Commit `07331aa`
- [x] **Etapa 5** — Testy čistej logiky (`test_pocasie.py`, 14/14 PASS, bez internetu). Commit `a7def26`
- [x] **Projekt 6 UZAVRETÝ** 🏁 — API · geocoding · web (Flask) · 7-dňová predpoveď · emoji · testy

---

## Stavanie s AI — Projekt 7: Nasadenie (deployment) ☁️
*(Cieľ: sprístupniť appku na internete. Nasadzujeme počasovú appku `web_pocasie.py`. Mapa ďalších
tém: [VIBE-CODING-MAPA.md](VIBE-CODING-MAPA.md), modul G.)*

- [x] **Etapa 1** — `requirements.txt` (zoznam balíčkov pre hosting), overené `pip install -r`
- [x] **Etapa 2** — rýchle zverejnenie cez **tunel (cloudflared)** — verejná URL `trycloudflare.com`, overené zvonku
- [x] **Etapa 3** — kód na **GitHub** (`silpet112/vibe-coding`) + nasadenie na **Render** (`pocasie.onrender.com`, live). Príprava: gunicorn + Procfile
- [x] **Etapa 4** — produkčný server (gunicorn na Renderi) + uzavrieť projekt
- [x] **Projekt 7 UZAVRETÝ** 🏁 — requirements · tunel (cloudflared) · GitHub · Render · gunicorn

---

## Stavanie s AI — Projekt 8: Prepojené tabuľky (relačná DB) 🔗
*(Cieľ: naučiť sa **relácie** — kategórie ako vlastná tabuľka, cudzí kľúč, `JOIN`. Mapa: modul H.)*

- [x] **Etapa 1** — Pochopiť relácie/cudzí kľúč/`JOIN` na čistej ukážke (`relacie_ukazka.py`, DB v pamäti)
- [x] **Etapa 2** — Relačná dátová vrstva `databaza_rel.py` (kategorie+vydavky, cudzí kľúč, výpis/súčty cez `JOIN`)
- [x] **Etapa 3** — Terminálové menu `vydavky_rel.py` nad relačnou DB (pridať/zobraziť/prehľad/kategórie cez `JOIN`)
- [x] **Etapa 4** — Testy relačnej logiky (`test_databaza_rel.py`, 8/8 PASS). Commit `e3e1b06`
- [x] **Projekt 8 UZAVRETÝ** 🏁 — relácie · cudzí kľúč · `JOIN` · testy

---

## Stavanie s AI — Projekt 9: Vlastný API + JavaScript 🌐
*(Cieľ: Flask vráti **JSON** (vlastný API) a stránka si ho cez **JavaScript `fetch`** vypýta bez reloadu. Mapa: modul I. Beží na porte 5002.)*

- [x] **Etapa 1** — Vlastný API `api_demo.py` (`/api/scitaj` vracia JSON, `jsonify`). Commit `cc8ea87`
- [x] **Etapa 2** — Stránka + **JavaScript `fetch`** → výsledok bez obnovenia (`scitanie.html`). Commit `8a0620e`
- [x] **Etapa 3** — Kalkulačka cez API (`/api/vypocet` +,−,×,÷, znova použitá `kalkulacka.py`) + výber operácie a Enter. Commit `f694156`
- [ ] **Etapa 4** — Testy + uzavrieť projekt
