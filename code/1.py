def random_number(s, minn, maxx, i):
    a = 1664525 + i*93876
    c = 1013904223 *i//83746345
    m = 2**32
    s = (a * s + c) % m
    return minn + (s % (maxx - minn + 1)), i + 1

s = 77
minn = 1409
maxx = 1489762

i = 0
for r in range(10):
    random_n, i = random_number(s, minn, maxx, i)
    print(random_n)