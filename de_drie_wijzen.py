# https://dodona.be/nl/courses/4195/series/46781/activities/113082360

# a+B+C=t
# a*b*c=t
# 0<a<=b<=c

# input = t,met twee cijfers na de komma


def find_gifts(total):
    for a in range(1, int(total * 100)):
        for b in range(1, int(total * 100)):
            a /= 100
            b /= 100
            c = total - a - b
            if c > 0 and round(a * b * c, 2) == total:
                return a, b, c
            a *= 100
            b *= 100
    return None

total = 65.52
a, b, c = find_gifts(total)
print(f"€{a:.2f} + €{b:.2f} + €{c:.2f} = €{a:.2f} x €{b:.2f} x €{c:.2f} = €{total:.2f}")
    
