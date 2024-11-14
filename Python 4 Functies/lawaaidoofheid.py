# https://dodona.be/nl/courses/4195/series/46780/activities/1563511392


def maximale_blootstelling(decibel):
    tijd = 0
    if decibel < 80:
        tijd = -1.0
    else:
        tijd = 28800 / (2 ** ((decibel - 80) // 3))
    return tijd
