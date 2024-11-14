# https://dodona.be/nl/courses/4195/series/46780/activities/1706631167

def csom(n):
    sommie=0
    while n > 9:
        sommie = 0
        for i in str(n):
            sommie += int(i)
        n = sommie
    
    return n
        