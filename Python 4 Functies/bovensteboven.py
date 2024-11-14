# https://dodona.be/nl/courses/4195/series/46780/activities/581452346


def bovensteboven(getal):
    getalString = str(getal)
    lengte = len(getalString)
    paren = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}    
    for i in range((lengte + 1) // 2):
        rechts = getalString[i]
        links = getalString[lengte - i - 1]
        
        if rechts not in paren or paren[rechts] != links:
            return False
    return True  

def volgende(getal):
    getal += 1
    while not bovensteboven(getal):
        getal += 1
    return getal 
