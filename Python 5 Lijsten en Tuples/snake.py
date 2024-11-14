# https://dodona.be/nl/courses/4195/series/46778/activities/1333299580


richtingen = ["<", "v", ">", "^"]


def beweeg(locatie, gekozenRichting):
    x = locatie[0]
    y = locatie[1]
    if gekozenRichting == richtingen[0]:
        x -= 1
    if gekozenRichting == richtingen[1]:
        y -= 1
    if gekozenRichting == richtingen[2]:
        x += 1
    if gekozenRichting == richtingen[3]:
        y += 1
    return (x, y)


def teruggekeerd(arr):
    move1 = arr[0]
    move2 = arr[1]
    locatie = (0, 0)
    locatie = beweeg(locatie, move1)
    locatie = beweeg(locatie, move2)
    return locatie == (0, 0)

def laatste_levende_positie(arr):
    geldigeZetten = 0
    locatie = (0,0)
    geldigeZet=False
    for i in range(len(arr)):
        if i!=0 and teruggekeerd((arr[i-1],arr[i])):
            geldigeZet = False
            break
        else:
            geldigeZet=True
        if geldigeZet:
            locatie= beweeg(locatie,arr[i])
            geldigeZetten+=1

        
        
    return(geldigeZetten,locatie[0],locatie[1])
        
print( laatste_levende_positie(['>', '<', '^']))
print(laatste_levende_positie(['v', '>', 'v', '<', '^', '^']))