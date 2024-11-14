# https://dodona.be/nl/courses/4195/series/46778/activities/818147392

import math

def driehoek(n):
    if not isinstance(n, int) or n < 0:
        raise AssertionError("ongeldig aantal rijen")
    volledigeDriehoek = []
    for i in range(n):
        if i == 0:
            volledigeDriehoek.append([1])
        else:
            rij = [1]
            for j in range(1, i):
                rij.append(
                    volledigeDriehoek[i - 1][j - 1] + volledigeDriehoek[i - 1][j]
                )
            rij.append(1)
            volledigeDriehoek.append(rij)
    return volledigeDriehoek


def zeshoek(i, j):
    i -= 1
    j -= 1
    zeshoek = []
    volledigeDriehoek = driehoek(i + 2)
    if (
        i <= 0
        or j <= 0
        or i >= len(volledigeDriehoek) - 1
        or j >= len(volledigeDriehoek[i]) - 1
    ):
        raise AssertionError("ongeldige interne positie")
    else:
        zeshoek.append(volledigeDriehoek[i - 1][j - 1])
        zeshoek.append(volledigeDriehoek[i - 1][j])
        zeshoek.append(volledigeDriehoek[i][j + 1])
        zeshoek.append(volledigeDriehoek[i + 1][j + 1])
        zeshoek.append(volledigeDriehoek[i + 1][j])
        zeshoek.append(volledigeDriehoek[i][j - 1])
    return zeshoek


def kwadraat(i, j):
    zoshoek = zeshoek(i, j)
    zin = ""
    for i in range(len(zoshoek)):
        if i != 0:
            zin += " x "
        zin += str(zoshoek[i])
    zin += f" = {math.prod(zoshoek)} = {int(math.sqrt(math.prod(zoshoek)))} x {int(math.sqrt(math.prod(zoshoek)))}"
    return zin
