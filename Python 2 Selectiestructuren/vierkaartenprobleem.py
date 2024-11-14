# https://dodona.be/nl/courses/4195/series/46782/activities/1345385696


from operator import truediv

correct=False
draaien=False
soort = input("")
if soort=='waarde':
    waarde = int( input(""))
    kleur=''
else:
    kleur = input('')
    waarde=''

if input("") == "ja":
    janee = True
else:
    janee = False

if soort=='waarde' :
    if waarde%2==0:
        draaien=True
    else:
        draaien=False
elif soort =="kleur":
    if kleur=='rood':
        draaien=False
    else:
        draaien=True
print(f"{'Juist' if draaien==janee else 'Fout'}: kaarten met {'kleur' if soort=='kleur' else 'waarde'} {kleur or waarde} moeten{'' if draaien else ' niet'} gedraaid worden.")