# https://dodona.be/nl/courses/4195/series/46781/activities/1047652305


rodeEnWitteSamen = int(input(''))
blauweEnWitteSamen = int(input(''))
groterOfKleiner= input('')
blauweRozen=0
rodeRozen=0
witteRozen=0
for blauweRozen in range(2, blauweEnWitteSamen + 1) :
    witteRozen = blauweEnWitteSamen - blauweRozen
    rodeRozen = rodeEnWitteSamen-witteRozen

    if witteRozen > 1 and blauweRozen > 1 and rodeRozen > 1:
        if (groterOfKleiner == '>' and (blauweRozen + rodeRozen) > (witteRozen + blauweRozen)) or \
           (groterOfKleiner == '<' and (blauweRozen + rodeRozen) < (witteRozen + blauweRozen)):
            print(blauweRozen)
            print(witteRozen)
            print(rodeRozen)
            break
        


