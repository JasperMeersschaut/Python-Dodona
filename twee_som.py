# https://dodona.be/nl/courses/4195/series/46773/activities/963734754


def twoSum(a, som):
    n = len(a)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] + a[j] == som:
                return (i, j)


def twoSumHash(a, som):
    n = len(a)
    d = dict()
    for i in range(0, n):
        complement = som - a[i]
        if complement in d:
            j = d[complement]
            return (j, i)
        else:
            d[a[i]] = i
