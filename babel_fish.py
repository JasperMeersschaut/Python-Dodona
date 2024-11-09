# https://dodona.be/nl/courses/4195/series/46777/activities/431253538


def vertalingToevoegen(woord,betekenis,collectie):
    collectie[woord]= betekenis

def vertaling(woord,collectie):
    if woord in collectie:
        return collectie[woord]
    else:
        return '???'