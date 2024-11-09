# https://dodona.be/nl/courses/4195/series/46778/activities/565313929


def eerste(oplossingArr):
    for i in range(len(oplossingArr)):
        for j in range(len(oplossingArr[i])):
            if oplossingArr[i][j] == 1:
                return (i, j)
            
def opvolger(oplossingArr,rij,kollom):
    getal = oplossingArr[rij][kollom]
    min_rij = rij - 1 if rij > 0 else 0
    min_kollom = kollom - 1 if kollom > 0 else 0
    max_rij = rij + 1 if rij + 1 < len(oplossingArr) else rij
    max_kollom = kollom + 1 if kollom + 1 < len(oplossingArr[rij]) else kollom

    for i in range(min_rij, max_rij + 1, 1) :
        for j in range(min_kollom, max_kollom + 1, 1) :
            if (oplossingArr[i][j] == getal + 1) :
                return (i, j)
    
    return (None, None)

def laatste(oplossingArr):
    (rij,kollom) = eerste(oplossingArr)
    if (rij,kollom) ==(None,None):
        return (None, None)
    while True:
        (volgende_rij, volgende_kollom) = opvolger(oplossingArr, rij, kollom)
        if volgende_rij is None or volgende_kollom is None :
            return (rij, kollom)
        (rij, kollom) = (volgende_rij, volgende_kollom)
    
def hidato(oplossingArr):
    (rij, kolom) = laatste(oplossingArr)
    if (rij, kolom) == (None, None):
        return False
    return oplossingArr[rij][kolom] == len(oplossingArr) * len(oplossingArr[0])
   
        
    
# print(eerste([[5, 4, 11, 12], [6, 10, 3, 2], [7, 8, 9, 1]]))
# print(opvolger([[5, 4, 11, 12], [6, 10, 3, 2], [7, 8, 9, 1]], 2, 3))
# print(opvolger([[44, 43, 42, 41, 39, 38], [45, 33, 32, 40, 36, 37], [46, 31, 34, 35, 4, 1], [47, 30, 29, 5, 3, 2], [11, 48, 28, 27, 6, 25], [12, 10, 8, 7, 26, 24], [13, 9, 17, 18, 20, 23], [14, 15, 16, 19, 22, 21]], 4, 1))
print(laatste([[5, 4, 11, 12], [6, 10, 3, 2], [7, 8, 9, 1]]))
print(laatste([[8, 14, 13, 12], [15, 1, 2, 11], [5, 3, 10, 16], [4, 6, 7, 9]]))
print(laatste(((18, 19, 20, 4, 5), (17, 1, 3, 6, 8), (16, 13, 2, 9, 7), (14, 15, 12, 11, 10))))
print(hidato([[5, 4, 11, 12], [6, 10, 3, 2], [7, 8, 9, 1]]))
print(hidato([[8, 14, 13, 12], [15, 1, 2, 11], [5, 3, 10, 16], [4, 6, 7, 9]]))