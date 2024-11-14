# https://dodona.be/nl/courses/4195/series/46783/activities/2071746302


appels = int(input())
VollePalletten = appels//700
VolleKistenMetRest = (appels%700)//20
RestAppels = (appels%700)%20

print(VollePalletten)
print(VolleKistenMetRest)
print(RestAppels)
