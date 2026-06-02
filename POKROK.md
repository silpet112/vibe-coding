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
**Aktuálna téma:** ✅ Jadro kurzu (Moduly A–C) hotové. Ďalej Modul D (pokročilé) alebo inštalácia nástrojov.
**Posledná lekcia:** C12 — Git a verzie, koncepty (2026-06-02) · praktický commit odložený (git nie je nainštalovaný)
**Ďalší krok:** **D13** (Modul D – pokročilé) — alebo praktické **inštalačné sedenie** (Git + Python → prvý reálny commit). Referencia: [CLAUDE-CODE-MAPA.md](CLAUDE-CODE-MAPA.md)

> Pozn.: Teraz ideme po **Claude Code ceste** (osnova nižšie). Pôvodná osnova programovania
> je zaparkovaná — ostáva nedotknutá v sekcii „Moja osnova" a vrátime sa k nej neskôr.

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

---

## Na zopakovanie
*(Veci, ktoré som už videl, ale ešte mi celkom nesadli — vrátime sa k nim.)*

- **Nainštalovať Python** — teraz na PC nie je (zistené v B8); doinštalujeme v programovacej
  časti, nech vieme písať aj v Pythone (zatiaľ používame PowerShell).
- **Nainštalovať Git** — teraz na PC nie je (zistené v C12); po inštalácii spravíme **prvý reálny
  commit** (`faktorial.ps1` + `POKROK.md`) a vyskúšame `/review`.

---

## Denník lekcií
*(Najnovší záznam navrch. Formát nižšie.)*

### Lekcia C12 — Git a verzie — 2026-06-02  ✅ Modul C (jadro)
**Čo sme prebrali:**
- Git: história verzií, commit (= uložená verzia s popisom), repo, diff, vetva; ako ho Claude používa; `/review`, `/code-review`. Rozdiel oproti rewind (trvalé vs. rýchle späť).

**Čo som pochopil:**
- Rozumiem, načo je git a commit. Explore ukázal, že git nie je nainštalovaný → praktický commit odložený. ✅ (koncepty)

**Praktická úloha:**
- Mal vzniknúť prvý commit — odložené, kým doinštalujeme git (pozri „Na zopakovanie").

**Kde sme skončili / ďalší krok:**
- Hotové jadro kurzu (Moduly A–C). Ďalej Modul D (pokročilé) alebo inštalačné sedenie (Git+Python).

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
- [x] C12. Git základ a ako ho Claude používa (`/review`, `/code-review`) — koncepty ✅, reálny commit po inštalácii gitu

**MODUL D — Prispôsobenie a rozšírenie** 🟣
- [ ] D13. settings.json a povolenia do hĺbky
- [ ] D14. Skills a vlastné slash príkazy
- [ ] D15. Subagenty (Agent)
- [ ] D16. MCP servery (externé nástroje)
- [ ] D17. Hooks (automatizácia pravidiel)

**MODUL E — Automatizácia a škálovanie** 🟣
- [ ] E18. Workflowy a multi-agent orchestrácia
- [ ] E19. Plánovanie a automatizácia (`/loop`, routines)
- [ ] E20. Súhrn najlepších návykov
