# https://dodona.be/nl/courses/4195/series/46782/activities/1647887074

winnaar = "niemand"
speler1 = input("Speler1: ").lower()
speler2 = input("Speler2: ").lower()

if speler1 == speler2:
    print("gelijkspel")

elif speler1 == "schaar":
    if speler2=="blad" or speler2=="hagedis":
        winnaar = "speler1"
    else:
        winnaar = "speler2"

elif speler1 == "blad":
    if speler2=="steen" or speler2=="spock":
        winnaar = "speler1"
    else:
        winnaar = "speler2"

elif speler1 == "steen":
    if speler2=="schaar" or speler2=="hagedis":
        winnaar = "speler1"
    else:
        winnaar = "speler2"

elif speler1 == "hagedis":
    if speler2=="spock" or speler2=="blad":
        winnaar = "speler1"
    else:
        winnaar = "speler2"

elif speler1 == "spock":
    if speler2=="schaar" or speler2=="steen":
        winnaar = "speler1"
    else:
        winnaar = "speler2"
if winnaar!="niemand":
    print(f"{winnaar} wint")