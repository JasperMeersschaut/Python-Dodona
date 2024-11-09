# https://dodona.be/nl/courses/4195/series/46781/activities/654951832

piraten = int(input(""))
kokosnoten = int(input(""))

for p in range(piraten):
    aapNoot = kokosnoten % piraten
    piraatNoot = kokosnoten//piraten
    print(
        f"{kokosnoten} noten = {piraatNoot} noten voor piraat#{p+1} en {"geen" if aapNoot == 0 else aapNoot} {"noot" if aapNoot == 1 else "noten"} voor de aap"
    )
    kokosnoten  = kokosnoten- aapNoot - piraatNoot
aapNoot = kokosnoten % piraten
print(
    f"elke piraat krijgt {kokosnoten//piraten} noten en {aapNoot if aapNoot>=1 else "geen"} {"noot" if aapNoot == 1 else "noten"} voor de aap"
)
