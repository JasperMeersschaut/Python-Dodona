# https://dodona.be/nl/courses/4195/series/46780/activities/862295437




def codeer(t, s):
    if s.isupper() and ' ' not in s:
        i = 0
        while len(t) != len(s):
            if i == len(s):
                i = 0
            s += s[i]
            i += 1
    code = ""
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(t)):
        if t[i].lower() not in alfabet:
            code += t[i]
        else:
            combo = (alfabet.index(t[i].lower()) + alfabet.index(s[i].lower())) % 26
            code += alfabet[combo].upper() if t[i].isupper() else alfabet[combo]
    return code

def decodeer(t, s):
    if s.isupper() and ' ' not in s:
        i = 0
        while len(t) != len(s):
            if i == len(s):
                i = 0
            s += s[i]
            i += 1
    code = ""
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(t)):
        if t[i].lower() not in alfabet:
            code += t[i]
        else:
            combo = (alfabet.index(t[i].lower()) - alfabet.index(s[i].lower())) % 26
            code += alfabet[combo].upper() if t[i].isupper() else alfabet[combo]
    return code

    
