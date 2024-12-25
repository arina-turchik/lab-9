def random_number(s, minn, maxx):
    # Линейный конгруэнтный генератор
    a = 1664525
    c = 1013904223
    m = 2**32
    s = (a * s + c) % m
    return minn + (s % (maxx - minn + 1))
print('Введите любое число, начальное число диапазона и конечное число диапазона:')
s = int(input())
minn = int(input())
maxx = int(input())

random_n = random_number(s, minn, maxx)
print(random_n)
