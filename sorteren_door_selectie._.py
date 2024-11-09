# https://dodona.be/nl/courses/4195/series/46775/activities/928829692

def selection_sort_vooraan(a):
    n = len(a)
    for i in range(n-1,1,-1):
        positie = i
        max = a[i]
        for j in range(i-1,0,-1):
           if a[j] >max:
               positie = j
               max=a[j]
        a[positie] = a[i]
        a[i] = max
        print(a)
        

