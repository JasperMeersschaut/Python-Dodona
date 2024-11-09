# https://dodona.be/nl/courses/4195/series/46780/activities/1131866318


def waardering(prijsBigMax, reeleKoers):
    macWisselKoers = prijsBigMax / 4.07
    procentWaardeerd = ((macWisselKoers - reeleKoers) / reeleKoers) * 100
    if procentWaardeerd <= -25:
        return "sterk ondergewaardeerd"
    elif procentWaardeerd <= -5:
        return "ondergewaardeerd"
    elif procentWaardeerd <= 5:
        return "ongeveer gelijk"
    elif procentWaardeerd <= 25:
        return "overgewaardeerd"
    else:
        return "sterk overgewaardeerd"


def wisselkoersanalyse(prijsBigMacFull, wisselKoers):
    prijsBigMacGesplitst = prijsBigMacFull.split()
    prijsBigMacPrijs = prijsBigMacGesplitst[0]
    prijsBigMacCurrency = ""
    for a in prijsBigMacGesplitst[1:]:
        prijsBigMacCurrency += a
        prijsBigMacCurrency += " "
        
    
    return f"De {prijsBigMacCurrency}is {waardering(float(prijsBigMacPrijs), wisselKoers)} ten opzichte van de dollar."
