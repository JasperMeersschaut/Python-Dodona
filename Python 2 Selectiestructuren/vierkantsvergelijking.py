# https://dodona.be/nl/courses/4195/series/46782/activities/1437422481


import math


a = float(input(""))
b = float(input(""))
c = float(input(""))
vierkantvergelijking = b**2 - 4 * a * c
if vierkantvergelijking < 0:
    print("geen wortels")
elif vierkantvergelijking == 0:
    print("een wortel")
    print(-b / (2 * a))
else:
    print("twee wortels")
    wortel1 = (-b + math.sqrt(vierkantvergelijking)) / (2 * a)
    wortel2 = (-b - math.sqrt(vierkantvergelijking)) / (2 * a)
    print(min(wortel1, wortel2))
    print(max(wortel1, wortel2))
