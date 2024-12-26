def random_number(s, minn, maxx):
    i = 0
    m = 2**32 
    while True:
        a = 1664525 + i * 93876
        c = 1013904223
        s = (a * s + c) % m
        yield minn + (s % (maxx - minn + 1))
        i += 1

s = 47
minn = 489
maxx = 594437

gen = random_number(s, minn, maxx)
for r in range(10):
    random_n = next(gen)
    print(random_n)
