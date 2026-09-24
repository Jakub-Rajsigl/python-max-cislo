from pathlib import Path

file_path = Path(__file__).with_name("poku.txt")

with file_path.open("r", encoding="utf-8") as soubor:
    cisla = []
    for radek in soubor:
        radek = radek.strip()
        if radek:
            cisla.append(int(radek))

if cisla:
    print(max(cisla))
else:
    print("Soubor neobsahuje žádné číslo.")
