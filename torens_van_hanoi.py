# https://dodona.be/nl/courses/4195/series/46779/activities/1092659960



def hanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * hanoi(n - 1) + 1
    
