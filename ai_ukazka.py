# ai_ukazka.py - Projekt 12, Etapa 1: appka, ktora zavola AI (Claude API).
# Posle prompt a vypise odpoved. API kluc berie z .env (ANTHROPIC_API_KEY).
# Spustenie:  python ai_ukazka.py
# Kluc ziskas na https://console.anthropic.com (je to platena sluzba).

import os

from dotenv import load_dotenv
import anthropic


def main():
    load_dotenv()  # nacita .env (vratane ANTHROPIC_API_KEY)

    # Bez kluca to nepojde - radsej pekne upozornime, nez by appka spadla.
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Chyba: chyba API kluc. Pridaj riadok ANTHROPIC_API_KEY=... do suboru .env.")
        print("(Kluc ziskas na https://console.anthropic.com)")
        return

    klient = anthropic.Anthropic()  # kluc si sam vezme z ANTHROPIC_API_KEY

    otazka = input("Spytaj sa AI nieco: ").strip() or "Pozdrav ma jednou vetou po slovensky."

    odpoved = klient.messages.create(
        model="claude-opus-4-8",          # aktualny model
        max_tokens=300,                   # max dlzka odpovede
        messages=[{"role": "user", "content": otazka}],
    )

    # odpoved.content je zoznam blokov; vypiseme tie textove
    print("\n--- AI odpoved ---")
    for blok in odpoved.content:
        if blok.type == "text":
            print(blok.text)


if __name__ == "__main__":
    main()
