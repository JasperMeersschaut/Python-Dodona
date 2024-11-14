# https://dodona.be/nl/courses/4195/series/46777/activities/370184940


def letterfrequenties(string):
    string = string.lower()
    dicionary = {}
    for karakter in string:
        if karakter.isalpha():
            if karakter in dicionary:
                dicionary[karakter] += 1
            else:
                dicionary[karakter] = 1
    return dicionary

def letterposities(string):
    string = string.lower()
    dictionary = {}
    for i, char in enumerate(string):
        if char.isalpha():
            if char in dictionary:
                dictionary[char].add(i)
            else:
                dictionary[char] = {i}
    return dictionary
