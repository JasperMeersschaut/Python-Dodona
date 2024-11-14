# https://dodona.be/nl/courses/4195/series/46777/activities/531231333


def dubbel(lijst):
    dicionary = {}
    for karakter in lijst:
            if karakter in dicionary:
                return karakter
                break
            else:
                dicionary[karakter] = 1
    return None

def dubbels(lijst):
    dictionary = {}
    eenmaalSet = set()
    meermaalSet = set()
    for karakter in lijst:
        if karakter in dictionary:
            meermaalSet.add(karakter)
            eenmaalSet.discard(karakter)
        else:
            dictionary[karakter] = 1
            eenmaalSet.add(karakter)
    return (eenmaalSet, meermaalSet)
    

print(dubbels([1, 2, 3, 4, 2]))