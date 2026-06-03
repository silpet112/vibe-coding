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
**Aktuálna téma:** 💰 Projekt 3 — Správca výdavkov (učím sa architektúru, .env a databázu — postupne po etapách A–E)
**Posledná lekcia:** Etapa D — **prehľady cez dotazy** (SQL `SUM` spolu, `GROUP BY` podľa kategórie, `WHERE ... LIKE` za mesiac), commit `eddd002` (2026-06-03) ✅
**Ďalší krok:** Etapa E — **automatické testy** pre logiku/databázu (na dočasnej DB) + **uzavrieť Projekt 3**. Plán: [STAVANIE-S-AI.md](STAVANIE-S-AI.md)

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

---

## Na zopakovanie
*(Veci, ktoré som už videl, ale ešte mi celkom nesadli — vrátime sa k nim.)*

- ~~Nainštalovať Python~~ — ✅ HOTOVO (2026-06-02, winget, Python 3.13.13). Funguje `python` aj `py`.
- ~~Nainštalovať Git~~ — ✅ HOTOVO (2026-06-02, winget v2.54); repo založené, prvý commit `554c82a`.

---

## Denník lekcií
*(Najnovší záznam navrch. Formát nižšie.)*

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
- [ ] **Etapa E** — Automatické testy + uzavrieť projekt
