# https://dodona.be/nl/courses/4195/series/46781/activities/2134730675


from inspect import getargvalues


getal = int(input(''))
aantalBeleefdeGetallen =0
for g in range(getal):
    getallenreeks = 0
    i = g
    if g!=getal-1:
        while getallenreeks<getal:
            i+=1
            getallenreeks+=i
            if getallenreeks==getal:
                aantalBeleefdeGetallen+=1 
    

print(aantalBeleefdeGetallen)