# https://dodona.be/nl/courses/4195/series/46780/activities/192047393

from webbrowser import get


def even_oneven(getal):
    even = 0
    oneven = 0
    for i in str(getal):
        if int(i) % 2 == 0:
            even += 1
        else:
            oneven += 1
    return(even, oneven)
 

def volgende(getal):
    even, oneven = even_oneven(getal)
    nieuwGetal = f"{even}{oneven}{len(str(getal))}"
    return int(nieuwGetal)

def stappen(getal):
    stappen = 0
    while getal != 123:
        getal = volgende(getal)
        stappen += 1

    return stappen


if __name__ == '__main__':
    import doctest
    doctest.testmod()

stappen(1234)