# https://dodona.be/nl/courses/4195/series/46782/activities/408865752


gewicht1 = input()
gewicht2 = input()
vervalst = 0
if gewicht1 == "evenwicht":
    if gewicht2 == "evenwicht":
        vervalst = 9
    if gewicht2 == "links":
        vervalst = 8
    if gewicht2 == "rechts":
        vervalst = 7
if gewicht1 == "links":
    if gewicht2 == "evenwicht":
        vervalst = 6
    if gewicht2 == "links":
        vervalst = 5
    if gewicht2 == "rechts":
        vervalst = 4
if gewicht1 == "rechts":
    if gewicht2 == "evenwicht":
        vervalst = 3
    if gewicht2 == "links":
        vervalst = 2
    if gewicht2 == "rechts":
        vervalst = 1

print(f"muntstuk #{vervalst} is vervalst")
