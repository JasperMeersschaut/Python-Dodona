# https://dodona.be/nl/courses/4195/series/46778/activities/197813628


def zeef(n):
    getallen = list(range(2, n + 1))
    m = getallen[0]
    while m < n:
        for i in getallen:
            if i % m == 0 and i != m:
                getallen.remove(i)
        if m == getallen[-1]:
            break
        m = getallen[getallen.index(m) + 1]
    return getallen

print(zeef(100)) 