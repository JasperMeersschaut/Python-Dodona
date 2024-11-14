# https://dodona.be/nl/courses/4195/series/46779/activities/854408577


def ggd(getal1, getal2):
    if getal2 == 0:
        return getal1
    else:
        return ggd(getal2, getal1 % getal2)