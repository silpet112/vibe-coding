# CLAUDE CODE — MAPA 🗺️
### Tvoja referencia / „učebnica" celého Claude Code

> Toto je text na **čítanie a opakovanie**. Nemusíš sa to učiť naspamäť — každú lekciu
> si spolu prejdeme naživo priamo tu v Claude Code. Tento súbor ti slúži, aby si sa
> kedykoľvek vedel vrátiť a pozrieť, „ako to bolo".
>
> Postup učenia a zaškrtávanie pokroku je v súbore **POKROK.md**.

---

## Ako používať túto mapu

- Mapa má **5 modulov (A–E)** a **20 lekcií**. Idú od najjednoduchšieho po pokročilé.
- Pri každej lekcii nájdeš:
  - **Čo to je** — vysvetlenie jednoducho po slovensky
  - **Prečo to potrebujem** — kde sa ti to v praxi zíde
  - **Kľúčové príkazy / skratky** — to najdôležitejšie
  - **Vyskúšaj si** — malá úloha, ktorú spravíme spolu
- Značky náročnosti:
  - 🟢 **základ** — toto chceš vedieť hneď
  - 🔵 **mierne pokročilé** — keď ti základ sadne
  - 🟣 **neskôr / pre pokročilých** — narastieš do toho, nie je to na začiatok

**Tvoje prostredie:** Windows 11 + VS Code + Claude Code. Skratky uvádzam pre Windows.
Keď si nie si istý, aké príkazy máš k dispozícii, vždy napíš `/help` — Claude ti ich ukáže.

---

## Rýchly slovníček (pojmy, ktoré sa hodia hneď) 🟢

| Pojem | Čo znamená (jednoducho) |
|---|---|
| **Terminál** | Čierne okno, kde sa píšu textové príkazy namiesto klikania. Vo VS Code ho otvoríš cez `` Ctrl+` ``. |
| **Príkaz (command)** | Riadok textu, ktorý počítaču povie, čo má spraviť (napr. `npm test`). |
| **Súbor (file)** | Jeden dokument s obsahom — napr. `POKROK.md` je súbor. |
| **Priečinok (folder/adresár)** | Krabica, v ktorej sú súbory. Tvoj projekt je priečinok `claude`. |
| **Kód** | Text napísaný v programovacom jazyku, ktorému rozumie počítač. |
| **CLI** | „Command-Line Interface" — ovládanie cez textové príkazy v termináli. |
| **IDE** | Program na písanie kódu (u teba **VS Code**). |
| **Repozitár / git** | Systém, ktorý si pamätá históriu zmien v projekte (verzie). Viac v Lekcii 12. |
| **Token / kontext** | „Pamäť" rozhovoru. Čím dlhší rozhovor, tým viac sa míňa. Viac v Lekcii 4. |
| **Slash príkaz** | Príkaz pre samotné Claude Code, začína lomkou — napr. `/help`, `/clear`. |
| **Agent** | Claude, ktorý nielen odpovedá, ale aj koná: číta súbory, mení ich, spúšťa príkazy. |

---

# MODUL A — Základy a prvé kroky 🟢

## Lekcia 1 — Čo je Claude Code a ako „rozmýšľa"

**Čo to je:**
Claude Code je AI **asistent na programovanie**, ktorý žije priamo v tvojom počítači
(v termináli alebo vo VS Code). Nie je to len chat — vie sám **čítať tvoje súbory,
upravovať ich, spúšťať príkazy a kontrolovať výsledok**.

Hlavný rozdiel oproti obyčajnému chatu je **agentický cyklus** — Claude pri každej úlohe
opakuje tri kroky:
1. **Získa kontext** — prečíta potrebné súbory, pochopí projekt
2. **Koná** — upraví súbory, spustí príkaz, vyhľadá v kóde
3. **Overí** — pozrie, či to vyšlo, prípadne spustí testy a opraví chyby

Kedykoľvek ho môžeš prerušiť a nasmerovať inam (klávesa **Esc**).

**Kde všade Claude Code beží** (rovnaký „mozog", iné rozhranie):
- **Terminál / CLI** — najsilnejšie, spúšťa sa príkazom `claude`
- **VS Code / JetBrains** — rozšírenie priamo v editore *(toto používaš ty)*
- **Desktop app** (Mac/Windows) — vizuálne rozdiely zmien, správa sedení
- **Web** (claude.ai/code) — v prehliadači, bez inštalácie
- **Slack, GitHub Actions** — automatizácia *(🟣 neskôr)*

**Prečo to potrebujem:** Aby si pochopil, že hovoríš s niečím, čo **samostatne pracuje**
na projekte — nie s vyhľadávačom. Preto mu treba dávať jasné úlohy a kontrolovať výsledok.

**Vyskúšaj si:** Povedz mi vlastnými slovami, čím sa líši „agent" od bežného chatu.

---

## Lekcia 2 — Prvý rozhovor a rozhranie

**Čo to je:**
S Claude Code sa rozprávaš **bežnou rečou** (pokojne po slovensky). Napíšeš úlohu,
on prečíta čo treba, premyslí to a buď ti ukáže navrhované zmeny, alebo si vypýta povolenie.

Pár pojmov:
- **Turn (kolo)** — jedna výmena: ty napíšeš → Claude odpovie/spraví → to je jeden turn.
- **Tool use (použitie nástroja)** — keď Claude číta súbor, hľadá v kóde alebo spúšťa
  príkaz, ukáže ti to ako krok („čítam súbor X"). Je to normálne, takto pracuje.
- **Diff** — farebné porovnanie „pred / po" pri úprave súboru. Zelená = pridané, červená = zmazané.

**Prečo to potrebujem:** Aby si sa nezľakol, keď Claude začne sám otvárať súbory a robiť
kroky — vidíš presne, čo robí, a máš to pod kontrolou.

**Kľúčové skratky:**
| Akcia | Skratka |
|---|---|
| Zastaviť Claude uprostred (kontext ostáva) | **Esc** |
| Odoslať správu | **Enter** |
| Nový riadok bez odoslania | **Shift+Enter** |
| Prejsť predchádzajúce moje správy | **↑** (šípka hore) |

**Vyskúšaj si:** Napíš mi jednoduchú otázku o tomto priečinku (napr. „čo je v tomto
projekte?") a sleduj, ako čítam súbory.

---

## Lekcia 3 — Povolenia a režimy (permission modes) 🟢

**Čo to je:**
Keďže Claude vie meniť súbory a spúšťať príkazy, **pýta si na to povolenie**. Ako často sa
pýta, určuje **režim**. Medzi režimami sa prepína klávesou **Shift+Tab** (alebo vo VS Code
klikom na ukazovateľ režimu dole pri poli na písanie).

| Režim | Pýta sa na... | Pre koho / kedy |
|---|---|---|
| **Default** | úpravy súborov aj príkazy | začiatočník, citlivá práca *(toto používaj na štart)* |
| **Accept edits** | len príkazy (úpravy súborov schvaľuje sám) | keď už dôveruješ a chceš menej prerušení |
| **Plan** | nič nemení — len číta a navrhuje plán | keď si chceš najprv premyslieť postup |
| **Auto** 🟣 | kontroluje to bezpečnostný „strážca" v pozadí | dlhé úlohy bez dozoru (pokročilé) |

**Prečo to potrebujem:** Je to tvoja **poistka**. V Default režime nič dôležité neprebehne
bez tvojho súhlasu. Keď niečomu nerozumieš — nechaj Default a čítaj, čo Claude pýta.

**Bezpečné návyky pre začiatočníka:**
- Začínaj v **Default**.
- Keď ti niečo nie je jasné, povolenie **odmietni** a opýtaj sa ma.
- Na *accept edits* prejdi, až keď budeš zmenám rozumieť.

**Vyskúšaj si:** Stlač **Shift+Tab** a pozri, ako sa mení režim (dole v okne). Vráť sa do Default.

---

## Lekcia 4 — Súbory a kontext

**Čo to je:**
- **Ako Claude číta súbory:** buď ho o to požiadaš („pozri sa do POKROK.md"), alebo súbor
  označíš znakom **`@`**. Napíš `@` a vyskočí ti zoznam súborov.
- **Kontext (kontextové okno):** je to celá „pamäť" aktuálneho rozhovoru — tvoje správy,
  odpovede, obsah prečítaných súborov, výstupy príkazov. Je **obmedzený**. Keď sa zaplní,
  Claude je pomalší a môže zabúdať staršie pokyny.

**Prečo to potrebujem:** Aby si vedel, prečo je dobré **začínať nové, nesúvisiace témy
„načisto"** — inak sa pamäť zahltí a kvalita klesá.

**Kľúčové príkazy:**
| Príkaz | Čo robí |
|---|---|
| `@nazov-suboru` | Pridá súbor do rozhovoru (Claude ho prečíta) |
| `/context` | Ukáže, čo všetko zaberá miesto v pamäti |
| `/clear` | Vymaže rozhovor a začne načisto (medzi nesúvisiacimi úlohami) |

> 💡 Pravidlo: **jedna téma = jeden rozhovor.** Keď prejdeš na úplne inú vec, daj `/clear`.

**Vyskúšaj si:** Napíš `/context` a pozrime sa spolu, čo aktuálne zaberá pamäť.

---

# MODUL B — Každodenná práca 🟢🔵

## Lekcia 5 — Slash príkazy, ktoré budeš používať denne

**Čo to je:** Príkazy pre samotné Claude Code. Napíš `/` a zobrazí sa zoznam.

| Príkaz | Čo robí |
|---|---|
| `/help` | Zoznam všetkých príkazov |
| `/clear` | Vyčistí rozhovor (nová téma) |
| `/init` | Vytvorí štartovací `CLAUDE.md` pre projekt (Lekcia 6) |
| `/config` | Nastavenia (téma, model…) |
| `/model` | Prepne AI model (napr. `sonnet` / `opus`) |
| `/review` | Skontroluje tvoje zmeny na chyby |
| `/rewind` | Vráti sa o krok späť (Lekcia 9) |
| `/context` | Čo zaberá pamäť |
| `/memory` | Zobrazí/upraví pamäťové súbory (CLAUDE.md, auto-pamäť) |
| `/resume` | Zoznam starších rozhovorov, pokračovať v jednom |

**Prečo to potrebujem:** Toto je tvoja každodenná „klávesnica". Stačí poznať týchto pár.

**Vyskúšaj si:** Napíš `/help` a spolu sa pozrieme, čo všetko máš k dispozícii.

---

## Lekcia 6 — `CLAUDE.md` — pamäť projektu

**Čo to je:**
`CLAUDE.md` je obyčajný textový súbor, ktorý Claude **prečíta na začiatku každého sedenia**.
Je to spôsob, ako mu dať **trvalé pokyny** o projekte — aby si nemusel stále opakovať to isté.

**Kam patrí:**
- `./CLAUDE.md` — v priečinku projektu (platí pre tento projekt)
- `~/.claude/CLAUDE.md` — v domovskom priečinku (platí pre všetky tvoje projekty)

**Čo doň písať:** príkazy, ktoré Claude neuhádne (ako sa spúšťajú testy/build), štýl kódu,
konvencie projektu, dôležité „nikdy nerob…".
**Čo doň NEpísať:** veci, ktoré vie odvodiť z kódu; dlhé výpisy. **Drž ho krátky** (ideálne
do ~200 riadkov) — každý riadok stojí pamäť.

> Bonus: Claude si aj sám automaticky ukladá poznámky (auto-pamäť). Pozrieš ich cez `/memory`.

**Prečo to potrebujem:** Aby Claude tvoj projekt „poznal" zakaždým a nerobil opakované chyby.

**Vyskúšaj si:** Skúsime spustiť `/init` a pozrieť sa, aký `CLAUDE.md` navrhne pre tento priečinok.

---

## Lekcia 7 — Ako dobre zadávať úlohy (prompting)

**Čo to je:** Spôsob, akým úlohu napíšeš, rozhoduje o výsledku. Štyri zlaté pravidlá:

1. **Buď konkrétny.** Namiesto „oprav prihlásenie" → „prihlásenie po zlom hesle ukáže
   bielu obrazovku; pozri sa do `@src/auth/` a oprav to."
2. **Daj príklad alebo vzor.** „Sprav to ako v `@src/auth/login.ts`."
3. **Žiadaj overenie.** „Napíš testy, spusti ich a oprav chyby." → Claude sa vie sám
   skontrolovať.
4. **Iteruj.** Nemusí to byť dokonalé na prvýkrát — povedz, čo zmeniť.

> ❌ „pridaj validáciu emailu"
> ✅ „pridaj funkciu `validateEmail`. Príklady: `user@example.com` → true, `invalid` → false.
>    Potom spusti testy."

**Prečo to potrebujem:** Konkrétne zadanie = správny výsledok na prvý raz. Vágne zadanie =
Claude háda a ty to opravuješ.

**Vyskúšaj si:** Skús to isté zadanie raz „vágne" a raz „konkrétne" a porovnáme rozdiel.

---

## Lekcia 8 — Plánovací režim (Plan mode) do hĺbky 🔵

**Čo to je:**
V plánovacom režime Claude **číta a skúma, ale nič nemení** — pripraví ti **plán** a ukáže
ho na schválenie. Až keď plán odobríš, prejde k vykonaniu.

Postup, ktorý sa oplatí: **Preskúmaj → Naplánuj → Koduj.**
1. Zapni Plan mode (Shift+Tab) a nechaj Claude pochopiť problém.
2. Pozri si plán (vo VS Code ho vieš otvoriť a upraviť cez **Ctrl+G**).
3. Schváľ → Claude začne písať kód.

> Toto sme práve teraz robili pri zostavovaní tvojej osnovy — bol to plánovací režim!

**Prečo to potrebujem:** Pri väčších alebo neistých zmenách je lacnejšie **opraviť plán**
ako opravovať hotový (nesprávny) kód.

**Kedy ho NEpoužívať:** pri drobnostiach (preklep, premenovanie) — tam rovno koduj.

**Vyskúšaj si:** Pri ďalšej väčšej úlohe skúsime najprv plán a potom vykonanie.

---

## Lekcia 9 — Vrátenie zmien a bezpečné experimentovanie 🔵

**Čo to je:**
Claude si robí **checkpointy** (záchytné body) pri každom kole. Vďaka tomu sa môžeš **vrátiť
späť** — k predchádzajúcemu stavu kódu aj rozhovoru. Vo VS Code podrž myš nad správou a
objaví sa tlačidlo na vrátenie.

**Kľúčové:**
| Akcia | Ako |
|---|---|
| Zastaviť uprostred | **Esc** |
| Vrátiť sa o krok späť (menu) | **Esc Esc** alebo `/rewind` |

Možnosti pri vrátení: vrátiť len kód, len rozhovor, alebo oboje.

**Prečo to potrebujem:** Aby si sa **nebál skúšať**. Keď sa niečo pokazí, jednoducho to
vrátiš — nič nezničíš natrvalo.

**Vyskúšaj si:** Spravíme malú zmenu a potom ju cez `/rewind` vrátime.

---

## Lekcia 10 — Správa sedení (sessions)

**Čo to je:**
Každý rozhovor (sedenie) sa **ukladá lokálne**. Môžeš sa k nemu vrátiť, pomenovať ho,
alebo začať nový. Mysli na sedenia ako na **šuplíky** — jeden šuplík = jedna téma/úloha.

**Kľúčové príkazy:**
| Príkaz | Čo robí |
|---|---|
| `/resume` | Vyber si zo zoznamu starších sedení |
| `claude --continue` | Pokračuj v poslednom (z terminálu) |
| `/clear` | Začni načisto v rámci sedenia |
| `/rename` | Pomenuj toto sedenie |

> ⚠️ Anti-pattern „kuchynský drez": riešiť 5 nesúvisiacich vecí v jednom rozhovore →
> pamäť sa zahltí, kvalita klesne. Radšej `/clear` medzi témami.

**Prečo to potrebujem:** Udržíš si poriadok a Claude zostane „bystrý".

**Vyskúšaj si:** Pomenujeme toto sedenie napr. `claude-code-ucenie`.

---

# MODUL C — Tvoje prostredie (VS Code) + Git 🔵

## Lekcia 11 — Claude Code vo VS Code

**Čo to je:** Grafické rozhranie Claude Code priamo v editore (toto používaš).

**Hlavné funkcie:**
- **Panel** s rozhovorom v bočnej lište.
- **Inline diffy** — navrhované zmeny vidíš pekne farebne v editore.
- **Výber textu = kontext** — keď si v editore označíš kód, Claude ho automaticky „vidí".
- **@-odkazy s riadkami** — napíš `@subor.py` alebo presne `@subor.py#5-10` (len riadky 5–10).
- **Plan mode** — klikni na ukazovateľ režimu dole; plán otvoríš/upravíš cez **Ctrl+G**.

**Užitočné skratky (Windows):**
| Akcia | Skratka |
|---|---|
| Prepnúť fokus medzi editorom a panelom Claude | **Ctrl+Esc** |
| Otvoriť v novej karte | **Ctrl+Shift+Esc** |
| Vložiť @-odkaz na aktuálny výber | **Alt+K** |
| Viacriadkový vstup | **Shift+Enter** |

**Prečo to potrebujem:** Je to tvoje **domáce prostredie** — oplatí sa poznať skratky,
ušetríš veľa času.

**Vyskúšaj si:** Označ pár riadkov v `POKROK.md` a opýtaj sa ma „čo to znamená?".

---

## Lekcia 12 — Git a verzie (základ) + ako ho Claude používa

**Čo to je:**
**Git** je systém, ktorý si pamätá **históriu zmien** projektu — vieš sa vrátiť k staršej
verzii, vidíš, čo sa kedy zmenilo, a môžeš pracovať vo viacerých „vetvách" naraz.

Základné pojmy:
- **commit** — uložená „fotka" stavu projektu s popisom, čo sa zmenilo
- **vetva (branch)** — samostatná línia práce (napr. nová funkcia bokom od hlavnej verzie)
- **diff** — rozdiel medzi dvoma stavmi (čo pribudlo/ubudlo)

**Claude vie git ovládať za teba:** vytvoriť commit s popisom, založiť vetvu, pripraviť
„pull request" (návrh na zlúčenie zmien).

**Kontrola kvality:**
| Príkaz | Čo robí |
|---|---|
| `/review` | Skontroluje tvoje zmeny na chyby |
| `/code-review` | Hlbšia kontrola rozdielu (dá sa aj `--fix` na opravu) |

> 🔗 Toto je prepojené s bodom 9 tvojej programovacej osnovy v POKROK.md (Git a verzionovanie).
> Tento projekt zatiaľ **nie je** git repozitár — keď budeš chcieť, založíme ho spolu.

**Prečo to potrebujem:** Git je záchranná sieť každého programátora — bez neho sa pracovať
nedá. Tu sa naučíš aspoň základ a ako ho Claude využíva.

**Vyskúšaj si:** Vysvetlíme si na príklade, čo je commit a prečo sa hodí.

---

# MODUL D — Prispôsobenie a rozšírenie 🟣 („level up")

## Lekcia 13 — `settings.json` a povolenia do hĺbky

**Čo to je:** Súbor s **nastaveniami** Claude Code. Tu vieš vopred povoliť dôveryhodné
príkazy (aby sa nepýtal), zakázať nebezpečné, nastaviť predvolený režim, model, premenné.

**Kde žije (od osobného po tímové):**
- `~/.claude/settings.json` — tvoje globálne nastavenia (všetky projekty)
- `.claude/settings.json` — nastavenia projektu (zdieľané s tímom cez git)
- `.claude/settings.local.json` — len tvoje pre tento projekt (nezdieľa sa)

**Príklad (povolenia):**
```json
{
  "permissions": {
    "allow": ["Bash(npm test)", "Read", "Edit"],
    "deny": ["Bash(rm -rf *)"],
    "defaultMode": "acceptEdits"
  }
}
```

**Prečo to potrebujem:** Aby si si Claude „naladil" — menej zbytočných otázok, viac bezpečia.

---

## Lekcia 14 — Skills a vlastné slash príkazy

**Čo to je:**
**Skill (zručnosť)** je tvoj **vlastný príkaz** — zabalený postup, ktorý Claude vyvolá
(automaticky alebo cez `/nazov`). Hodí sa, keď stále dokola opakuješ ten istý postup.

- Žijú v `.claude/skills/nazov/SKILL.md` (projekt) alebo `~/.claude/skills/…` (globálne).
- Načítajú sa **až keď ich treba** — takže nezaberajú pamäť zbytočne (na rozdiel od `CLAUDE.md`).

**Prečo to potrebujem:** Zautomatizuješ si opakované veci („sprav release checklist",
„priprav nový komponent podľa nášho vzoru").

---

## Lekcia 15 — Subagenty (Agent)

**Čo to je:**
**Subagent** je samostatný Claude, ktorému hlavný Claude **deleguje** vedľajšiu úlohu
(napr. prehľadať veľa súborov). Pracuje vo **vlastnej pamäti**, takže nezahlcuje ten tvoj
hlavný rozhovor — vráti len zhrnutie.

- Zabudované typy: **Explore** (hľadanie), **Plan** (návrh plánu), **general-purpose** a ďalšie.
- Vlastné si vyrobíš v `.claude/agents/nazov.md`.
- Dá sa spustiť aj **viac naraz** (paralelne) — rýchlejšie pri veľkom prehľadávaní.

> Pri zostavovaní tvojej osnovy som použil dva výskumné subagenty naraz — preto to bolo rýchle.

**Prečo to potrebujem:** Šetrí pamäť a čas pri väčších úlohách.

---

## Lekcia 16 — MCP servery (pripojenie externých nástrojov)

**Čo to je:**
**MCP** (Model Context Protocol) je „zásuvka", cez ktorú Claude pripojíš k **externým
službám** — GitHub, Gmail, Kalendár, Notion, databázy, Google Drive a stovky ďalších.
Potom vie reálne čítať/písať do týchto nástrojov.

- Pridanie (z terminálu): `claude mcp add …`
- Príklady: „nájdi v databáze zákazníkov bez nákupu za 90 dní", „priprav koncept emailu…".

> V tvojom prostredí už nejaké pripojenia vidno (Gmail, Kalendár, Drive, Notion, ClickUp…).
> Budú pre teba užitočné neskôr.

**Prečo to potrebujem:** Aby Claude nepracoval len so súbormi, ale aj s tvojimi reálnymi nástrojmi.

---

## Lekcia 17 — Hooks (automatizácia pravidiel)

**Čo to je:**
**Hook** je tvoj príkaz, ktorý sa **automaticky a spoľahlivo spustí** pri určitej udalosti —
napr. *po každej úprave súboru*, *na začiatku sedenia*, *pred spustením príkazu*.

Rozdiel oproti `CLAUDE.md`: pokyny v CLAUDE.md sú „odporúčania", ale **hook sa vykoná vždy**.

**Typické použitie:** automaticky naformátovať kód po úprave; zablokovať úpravu chráneného
súboru; poslať upozornenie, keď Claude niečo potrebuje.

Nastavujú sa v `settings.json`.

**Prečo to potrebujem:** Vynútiš pravidlá projektu bez toho, aby si na ne musel myslieť.

---

# MODUL E — Automatizácia a škálovanie 🟣 (power user)

## Lekcia 18 — Workflowy a multi-agent orchestrácia

**Čo to je:**
**Workflow** je skript (v JavaScripte), ktorý **riadi veľa subagentov naraz** podľa
presného postupu. Hodí sa na **veľké úlohy** — migrácia 100 súborov, audit celého projektu,
dôkladný research s krížovou kontrolou.

- Požiadaš o to slovami („sprav workflow, ktorý skontroluje všetky API endpointy…").
- Priebeh sleduješ cez `/workflows`.

**Prečo to potrebujem:** Keď je úloha priveľká na jeden rozhovor, workflow ju zvládne na šírku.

---

## Lekcia 19 — Plánovanie a automatizácia v čase

**Čo to je:** Spustiť úlohu **opakovane** alebo **neskôr**.

| Nástroj | Na čo |
|---|---|
| `/loop 5m <úloha>` | Opakuj úlohu každých 5 min (napr. „skontroluj, či dobehol build") |
| `/loop` (bez času) | Claude si sám zvolí, ako často (podľa diania) |
| `/schedule` (routines) | Naplánované behy „v oblaku" (aj keď máš počítač vypnutý) |
| pripomienky | „o 45 minút mi pripomeň skontrolovať testy" |

**Prečo to potrebujem:** Nemusíš sedieť a čakať — Claude pracuje/kontroluje za teba.

---

## Lekcia 20 — Súhrn najlepších návykov

**Čo to je:** Päť vecí, ktoré odlišujú začiatočníka od skúseného používateľa:

1. **Spravuj pamäť (kontext).** `/clear` medzi nesúvisiacimi úlohami. Toto je #1 vec, ktorá
   drží kvalitu vysoko.
2. **Vždy daj „kontrolu".** Testy, build, screenshot — nech sa Claude vie sám overiť.
3. **Najprv plán, potom kód** pri väčších/neistých zmenách.
4. **Buď konkrétny** a daj príklady.
5. **Oprav skoro.** Keď si Claude opravoval 2× tú istú vec a nejde to → `/clear` a napíš
   lepšie zadanie.

**Bonus — writer/reviewer:** dôležitý kód nechaj skontrolovať v **novom, čistom rozhovore**
(`/clear` alebo nové sedenie) — „svieži pohľad" nájde viac chýb.

**Prečo to potrebujem:** Toto je „jazda na bicykli" — keď ti to sadne, Claude Code je
nečakane výkonný a príjemný nástroj.

---

# 📎 Rýchle karty (cheat sheet)

### Najdôležitejšie slash príkazy
`/help` · `/clear` · `/init` · `/config` · `/model` · `/review` · `/rewind` · `/context` ·
`/memory` · `/resume` · `/rename` · `/permissions`

### Klávesové skratky (Windows / VS Code)
| Akcia | Skratka |
|---|---|
| Prepnúť režim povolení | **Shift+Tab** |
| Zastaviť Claude | **Esc** |
| Vrátiť sa späť (rewind) | **Esc Esc** |
| Nový riadok | **Shift+Enter** |
| Otvoriť terminál vo VS Code | **`` Ctrl+` ``** |
| Fokus editor ↔ panel Claude | **Ctrl+Esc** |
| Vložiť @-odkaz na výber | **Alt+K** |
| Otvoriť/upraviť plán | **Ctrl+G** |

### Kde čo žije (súbory a priečinky)
```
./CLAUDE.md                 pokyny pre tento projekt
~/.claude/CLAUDE.md         pokyny pre všetky projekty
./.claude/settings.json     nastavenia projektu
~/.claude/settings.json     tvoje globálne nastavenia
./.claude/skills/           tvoje vlastné príkazy (skills)
./.claude/agents/           tvoje vlastné subagenty
```

### Časté chyby začiatočníka → riešenie
| Chyba | Riešenie |
|---|---|
| Všetko v jednom rozhovore | `/clear` medzi témami |
| Pridlhý `CLAUDE.md` | skráť, nechaj len podstatné |
| Vágne zadanie | konkrétne + príklad + „over to" |
| Žiadna kontrola | nechaj spustiť testy/build |
| Oprava dokola | po 2× radšej `/clear` a nový prompt |

---

## 📚 Oficiálne zdroje (ak si budeš chcieť čítať aj sám)
- Prehľad: https://code.claude.com/docs/en/overview
- Quickstart: https://code.claude.com/docs/en/quickstart
- Najlepšie návyky: https://code.claude.com/docs/en/best-practices
- Pamäť (CLAUDE.md): https://code.claude.com/docs/en/memory
- Režimy povolení: https://code.claude.com/docs/en/permission-modes
- VS Code: https://code.claude.com/docs/en/vs-code

> Pozn.: presné názvy skratiek/príkazov sa môžu drobne líšiť podľa verzie. Keď si nie si
> istý, `/help` ti vždy ukáže aktuálnu pravdu.
