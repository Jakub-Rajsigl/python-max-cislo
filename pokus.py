import os

with open(os.sep.join(["python-max-cislo", "poku.txt"])) as soubor:
    radky = soubor.readlines()

if len(radky) <= 0:
    print("Soubor je prázdný!")
    exit()

max = int(radky[0].strip())
for radek in radky:
    cislo = int(radek.strip())
    if cislo > max:
        max = cislo

print(f"Nejvyšší hodnota v souboru je: {max}")