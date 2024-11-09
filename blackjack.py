# https://dodona.be/nl/courses/4195/series/46781/activities/1319193582

kaart = int(input(''))
totaal = kaart
while totaal < 21 and kaart != 0:
    kaart = int(input(''))
    totaal += kaart
if kaart==0:
    print(f"Voorzichtig gespeeld ({totaal})")
elif totaal>21:
    print(f"Verbrand ({totaal})")
else:
    print("Gewonnen!")