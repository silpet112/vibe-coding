# VIBE CODING — MAPA ĎALŠÍCH LEKCIÍ 🗺️🚀
### Čo sa ešte naučiť (cesta po Projekte 6)

> Toto je text na **čítanie a orientáciu** — nie na učenie naspamäť. Každú tému prejdeme naživo
> ako samostatnú lekciu + malý projekt (presne ako API a deployment). Postup a zaškrtávanie je
> v **POKROK.md**, recept na stavanie v **STAVANIE-S-AI.md**.

---

## Čo už mám hotové ✅
Režisérsky cyklus · terminálové appky · JSON · **databáza (SQLite, CRUD)** · `.env` · **vrstvená
architektúra** · automatické testy · **web (Flask, HTML, CSS)** · query string (filter) · **API**
(volanie cudzích služieb). 6 dokončených projektov + skill `/app`.

Táto mapa je o tom, **čo ešte príde**.

## Legenda náročnosti
- 🟢 **základ** — zvládneš čoskoro, hodí sa hneď
- 🔵 **mierne pokročilé** — keď ti základ sadne
- 🟣 **neskôr / pre pokročilých** — narastieš do toho

## Ako čítať každú lekciu
Pri každej téme nájdeš: **Čo to je** · **Prečo to potrebujem** · **Čo by sme postavili** (mini-projekt
alebo rozšírenie existujúcej appky).

---

## Modul F — Verzionovanie a spolupráca 🌿

### F1. Git hlbšie — vetvy a návrat zmien 🔵
- **Čo to je:** *vetva (branch)* = bočná línia, kde skúšaš zmeny bez toho, aby si pokazil hlavnú verziu.
- **Prečo:** bezpečné experimentovanie; návrat, keď sa niečo pokazí.
- **Čo by sme postavili:** na existujúcej appke skúsime novú funkciu vo vetve a spojíme ju späť.

### F2. GitHub — kód v cloude 🔵
- **Čo to je:** GitHub = web, kam *nahráš (push)* svoj git repozitár.
- **Prečo:** záloha kódu mimo PC, história online, zdieľanie, a je to **predpoklad pre mnohé hostingy** (deployment).
- **Čo by sme postavili:** založíme GitHub repo a nahráme naň tvoje projekty.

### F3. Spolupráca (pull requesty) 🟣
- **Čo to je:** spôsob, ako navrhnúť zmenu a nechať ju schváliť.
- **Prečo:** keď na projekte robí viac ľudí (alebo „ja + budúce ja").

---

## Modul G — Nasadenie a prevádzka (deployment) ☁️ — *Projekt 7 (ide hneď)*

### G1. Localhost vs internet 🟢
- **Čo to je:** prečo `127.0.0.1` vidí len tvoj počítač. *(Koncept už máš!)*

### G2. Tunel (ngrok) 🔵
- **Čo to je:** nástroj, čo spraví **dočasnú verejnú adresu** k tvojmu lokálnemu serveru.
- **Prečo:** rýchlo ukázať appku kamarátovi bez hostingu.
- **Čo by sme postavili:** sprístupníme počasovú appku na verejnej URL za pár minút.

### G3. Hosting (PythonAnywhere / Render) 🔵
- **Čo to je:** cudzí server, kde appka beží **stále** (aj keď máš PC vypnutý).
- **Prečo:** „naozajstné" nasadenie s trvalou verejnou adresou.
- **Čo by sme postavili:** nasadíme počasovú appku na bezplatný hosting.

### G4. Produkčný server, doména, HTTPS, env v produkcii 🔵
- **Čo to je:** prečo `debug=True` nie je na produkciu (gunicorn/waitress); vlastná **doména**; **HTTPS**
  (zámok v prehliadači); tajomstvá cez premenné prostredia aj na serveri.
- **Prečo:** bezpečná a dôveryhodná verejná prevádzka.

---

## Modul H — Dáta a databázy hlbšie 🗄️

### H1. Prepojené tabuľky (relácie, cudzí kľúč, JOIN) 🔵
- **Čo to je:** viac tabuliek, ktoré sa **odkazujú** na seba (napr. *kategórie* ako vlastná tabuľka, na ktorú ukazujú *výdavky*).
- **Prečo:** takto vyzerajú reálne databázy; menej opakovania, čistejšie dáta.
- **Čo by sme postavili:** vo výdavkoch spravíme kategórie ako samostatnú tabuľku a spojíme ich cez `JOIN`.

### H2. Import / export dát (CSV, Excel) 🟢
- **Čo to je:** načítať/uložiť dáta do tabuľkového súboru.
- **Prečo:** dáta vieš preniesť, zálohovať, otvoriť v Exceli.
- **Čo by sme postavili:** „Exportuj výdavky do CSV" (otvoríš v Exceli).

### H3. Zmeny schémy / migrácie 🟣 · H4. Čo je ORM 🟣
- **Čo to je:** ako bezpečne meniť stĺpce v už existujúcej databáze; ORM = práca s DB cez objekty namiesto SQL.
- **Prečo:** udržateľnosť väčších projektov.

---

## Modul I — Web hlbšie (frontend + backend) 🌐

### I1. Šablóny hlbšie — spoločná „base" šablóna 🟢
- **Čo to je:** jedna kostra stránky (hlavička/päta), ktorú **dedia** ostatné stránky.
- **Prečo:** neopakuješ HTML; zmena na jednom mieste.

### I2. JavaScript základy 🔵
- **Čo to je:** jazyk, ktorý beží **v prehliadači** a robí stránku interaktívnou (tlačidlá, reakcie bez načítania).
- **Prečo:** doteraz robil všetko server; JS pridá živosť na strane používateľa.

### I3. Dynamické stránky bez reloadu (fetch) 🔵
- **Čo to je:** prehliadač si **sám** vypýta dáta z tvojho servera a prekreslí časť stránky.
- **Čo by sme postavili:** počasie sa načíta bez obnovenia celej stránky.

### I4. Tvoj vlastný API 🔵
- **Čo to je:** tvoj Flask vráti **JSON** (nie HTML) — staneš sa *poskytovateľom* API, nielen spotrebiteľom.
- **Prečo:** základ moderných appiek (frontend + API backend).
- **Čo by sme postavili:** endpoint `/api/pocasie?mesto=...`, ktorý vráti JSON.

### I5. Responzívny dizajn / CSS rámce 🔵
- **Čo to je:** aby stránka vyzerala dobre aj na mobile (napr. cez hotový CSS rámec).

---

## Modul J — Používatelia a bezpečnosť 🔐

### J1. Prihlásenie a registrácia 🔵
- **Čo to je:** používateľské účty, heslá (bezpečne uložené), *sessions* (appka si pamätá, kto je prihlásený).
- **Prečo:** každá appka „pre ľudí" to potrebuje; súkromné dáta na používateľa.
- **Čo by sme postavili:** výdavky len pre prihláseného používateľa.

### J2. Základy bezpečnosti 🔵
- **Čo to je:** validácia vstupov, **SQL injection** (parametrizované dotazy už používame ✅), tajomstvá mimo kódu, HTTPS.
- **Prečo:** aby sa appka nedala ľahko zneužiť.

### J3. Oprávnenia (kto čo smie) 🟣
- **Čo to je:** rozlíšiť bežného používateľa a admina.

---

## Modul K — Kvalita a profesionálne návyky 🛠️

### K1. Debugging a čítanie chýb + logovanie 🟢
- **Čo to je:** ako čítať *traceback* (chybovú hlášku) a nájsť príčinu; zapisovanie *logov*.
- **Prečo:** rýchlejšie opravíš, čo sa pokazí (aj na nasadenej appke).

### K2. requirements.txt + virtuálne prostredie (venv) 🟢
- **Čo to je:** zoznam balíčkov projektu + izolované „prostredie" pre každý projekt.
- **Prečo:** appka sa rozbehne aj inde (a hosting to očakáva).
- **Čo by sme postavili:** pridáme `requirements.txt` k appkám (potrebné pred deploymentom).

### K3. Testovací rámec pytest 🔵
- **Čo to je:** štandardný nástroj na testy (namiesto nášho domáceho `skontroluj`).
- **Prečo:** profi spôsob, viac možností.

### K4. Refaktoring / čistý kód 🔵 · K5. Code review 🟢
- **Čo to je:** upratať kód bez zmeny správania; nechať si zmeny skontrolovať (`/code-review` už poznáš).

---

## Modul L — AI a automatizácia (nadstavba vibe codingu) 🤖

### L1. Volať AI model z vlastnej appky 🔵🟣
- **Čo to je:** tvoja appka pošle otázku AI (napr. **Claude API**) a použije odpoveď — cez API kľúč v `.env`.
- **Prečo:** appka, ktorá „rozmýšľa" (zhrnie text, odpovedá, triedi).
- **Čo by sme postavili:** appka, čo k počasiu pridá vetu „čo si obliecť" od AI.

### L2. Naplánované úlohy / automatizácia 🔵
- **Čo to je:** spustiť úlohu pravidelne (napr. ráno poslať počasie).

### L3. Notifikácie / e-maily z appky 🔵 · L4. MCP / pripojenie nástrojov 🟣
- **Čo to je:** appka pošle e-mail/správu; pripojenie hotových nástrojov (koncept z kurzu Claude Code).

---

## 🧭 Odporúčané poradie (dá sa kedykoľvek zmeniť)
1. **G — Deployment** (Projekt 7, ide hneď) 🚀
2. **F — GitHub** (záloha + zdieľanie kódu, predpoklad pre hosting)
3. **K — venv + requirements + debugging** (zdravé základy)
4. **H — prepojené tabuľky** (databáza hlbšie)
5. **I — vlastný API + JavaScript** (moderný web)
6. **J — prihlasovanie** (používatelia a bezpečnosť)
7. **L — AI vo vlastnej appke** (čerešnička 🍒)

> Poradie je len odporúčanie — pokojne skočíme na tému, ktorá ťa práve láka. Po každej lekcii
> zaškrtneme pokrok v POKROK.md, presne ako doteraz.
