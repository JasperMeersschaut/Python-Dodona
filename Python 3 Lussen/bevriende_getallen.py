# https://dodona.be/nl/courses/4195/series/46781/activities/1258720912


getal1 = int(input(''))
getal2 = int(input(''))

delersGetal1 =0
delersGetal2=0

for g in range(getal1):
    if getal1%(g+1) == 0:
        delersGetal1+=g+1
    if g > getal1/2:
        break

for g in range(getal2):
    if getal2%(g+1) == 0:
        delersGetal2+=g+1
    if g > getal2/2:
        break
bevriendeGetallen = delersGetal1==getal2 and delersGetal2==getal1

print(f'{getal1} en {getal2} zijn {"" if bevriendeGetallen else "geen"} bevriende getallen') 