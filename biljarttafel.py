# https://dodona.be/nl/courses/4195/series/46781/activities/364433585


hoogte = int(input(""))
breedte = int(input(""))

balLocatie = [0, 0]
goal = False
richtingHorizontaal = 1
richtingVerticaal = 1
while not goal:
    balLocatie[0] += richtingHorizontaal
    balLocatie[1] += richtingVerticaal
    if balLocatie == [breedte, hoogte]:
        print(f"rechterbovenpocket ({balLocatie[0]}, {balLocatie[1]})")
        goal = True
    elif balLocatie == [0, 0]:
        print(f"linkeronderpocket ({balLocatie[0]}, {balLocatie[1]})")
        goal = True
    elif balLocatie == [0, hoogte]:
        print(f"linkerbovenpocket ({balLocatie[0]}, {balLocatie[1]})")
        goal = True
    elif balLocatie == [breedte, 0]:
        print(f"rechteronderpocket ({balLocatie[0]}, {balLocatie[1]})")
        goal = True

    elif balLocatie[0] == breedte:
        print(f"rechterband ({balLocatie[0]}, {balLocatie[1]})")
        richtingHorizontaal = -1
    elif balLocatie[1] == hoogte:
        print(f"bovenband ({balLocatie[0]}, {balLocatie[1]})")
        richtingVerticaal = -1

    elif balLocatie[0] == 0:
        print(f"linkerband ({balLocatie[0]}, {balLocatie[1]})")
        richtingHorizontaal = 1
    elif balLocatie[1] == 0:
        print(f"onderband ({balLocatie[0]}, {balLocatie[1]})")
        richtingVerticaal = 1
