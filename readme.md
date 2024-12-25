# Лабораторная работа №9
### Вариант №11
## Ход работы:
1. Разобраться в работе генераторов.
2. Написать генератор для своего варианта.
3. Отправить решение задачи на `github`.
## Задача
### Написать генератор случайных чисел в заданном диапазоне. Не использовать готовые реализации ГПСЧ.
## Решение:
```
def random_number(s, minn, maxx):
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
```
## Источники:
[evil-teacher](https://evil-teacher.on-fleek.app/prog_pm/term1/lab09/)  
[generators](https://github.com/still-coding/se_python_snippets/blob/main/03_advanced/generators.py)  
[линейный конгруэнтный метод](https://ru.wikipedia.org/wiki/%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BE%D0%BD%D0%B3%D1%80%D1%83%D1%8D%D0%BD%D1%82%D0%BD%D1%8B%D0%B9_%D0%BC%D0%B5%D1%82%D0%BE%D0%B4)
