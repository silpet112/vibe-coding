---
name: app
description: Spusti webovú appku Výdavky (Flask) a otvor ju v prehliadači — naštartuje server na pozadí a otvorí http://127.0.0.1:5000.
---

Keď ťa vyvolá `/app`, spusti používateľovi jeho webovú appku Výdavky a otvor ju v prehliadači.
Komunikuj po slovensky, jednoducho.

Postup:
1. Spusti Flask server **na pozadí** (run_in_background = true), aby neblokoval ďalšiu prácu:
   v priečinku projektu spusti `python app.py`.
2. Otvor stránku v predvolenom prehliadači (Windows, PowerShell):
   `Start-Process "http://127.0.0.1:5000"`.
   - Ak by sa stránka načítala skôr, než server nabehne, počkaj chvíľu a skús `Start-Process`
     znova (server po štarte vypíše „Running on http://127.0.0.1:5000").
3. Stručne povedz používateľovi:
   - že appka beží a stránka sa otvorila v prehliadači,
   - že **server beží na pozadí**, takže môže ďalej pracovať,
   - ako ho **zastaviť**: stačí povedať „zastav appku" (zastavíš proces na pozadí), prípadne
     `Ctrl+C` v termináli, kde beží.

Poznámky:
- Príkaz spúšťaj z koreňa projektu (kde je `app.py`). Netreba `cd`, pracovný priečinok je správny.
- Ak `app.py` neexistuje alebo zlyhá štart, zisti príčinu z výstupu a vysvetli to po slovensky.
- Ak už server beží (port 5000 obsadený), nespúšťaj druhý — len otvor stránku cez `Start-Process`.
