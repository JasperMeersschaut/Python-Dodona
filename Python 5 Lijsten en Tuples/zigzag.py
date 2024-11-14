# https://dodona.be/nl/courses/4195/series/46778/activities/2038783829


def iszigzag(arr):
    for i in range(len(arr) - 1):
        if i % 2 == 0:
            if arr[i] < arr[i + 1]:
                return False
        else:
            if arr[i] > arr[i + 1]:
                return False
    return True

def zigzag_traag(lijst):
    lijst.sort()
    for i in range(0, len(lijst)-1, 2):
        lijst[i], lijst[i + 1] = lijst[i + 1], lijst[i]

def zigzag_snel(lijst):
    for i in range(0, len(lijst) ,2):
        if i > 0 and lijst[i]<lijst[i-1]:
            lijst[i], lijst[i - 1] = lijst[i - 1], lijst[i]
        if i < len(reeks) - 1 and lijst[i]<lijst[i+1]:
            lijst[i], lijst[i + 1] = lijst[i + 1], lijst[i]
        
reeks = [10, 90, 49, 2, 1, 5, 23]
zigzag_snel(reeks)
print(reeks)