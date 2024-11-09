# https://dodona.be/nl/courses/4195/series/46775/activities/875119571


def zoekBinair(rij,zoekItem):
    n=len(rij)
    l=0
    r=n-1
    while l != r :
        print(f"{l}, {r}")
        m = (l+r)//2
        if rij[m] > zoekItem :
            l = m + l
        else:
            r = m
    if rij[l] == zoekItem:
        index = 1
    else: 
        index = -1
    return index