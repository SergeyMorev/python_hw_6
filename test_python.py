import math
from math import sqrt, pow, hypot

# Тестирование встроенных функций.


def test_pi_identical():
    # math.pi - это константа. Как тестировать константу?
    assert 3.141592653589793 == math.pi


def test_sqrt_1():
    # Корень из квадрата должен давать исходное число
    for a in range(0, 10, 1):
        assert math.sqrt(a * a) == a


def test_sqrt_2():
    # Умножение корня на себя должно давать исходное число
    assert [sqrt(a) * sqrt(a) == a for a in range(0, 10, 1)]


def test_sqrt_constants():
    # Проверка корня на известных константах
    assert 0 == sqrt(0)
    assert 0.0 == sqrt(0.0)

    assert 1 == sqrt(1)
    assert 1.0 == sqrt(1.0)

    assert 2 == sqrt(4)
    assert 2.0 == sqrt(4.0)

    assert 3 == sqrt(9)
    assert 3.0 == sqrt(9.0)

    assert 4 == sqrt(16)
    assert 4.0 == sqrt(16.0)

    assert 100 == sqrt(10000)
    assert 100.0 == sqrt(10000.0)


def test_pow_multiply():
    # Проверка степени через умножение числа самого на себя в цикле
    def my_power(a, exp):
        res = 1
        for _ in range(exp):
            res *= a
        return res

    for a in range(5):
        for i in range(0, 11):
            assert pow(a, i) == my_power(a, i)


def test_fraction_pow():
    # Проверка дробной степень 0.5 через функцию корня
    for i in range(1000):
        assert pow(float(i), 0.5) == sqrt(float(i))


def test_hypot_constants():
    # Проверка hypot через константы (известные треугольники)
    assert 5 == hypot(3, 4)

    assert 5.0 == hypot(3.0, 4.0)


def test_hypot_multiply():
    # Проверка hypot через квадраты (без извлечения корня)
    epsilon = 1e-10     # Точность сравнения

    for a in range(50, 100):
        for b in range(1, 60):
            h = hypot(a, b)
            assert abs(h*h - (a*a + b*b)) < epsilon, f'a={a}, b={b}, h={h}'


source_data = ['1', '2', '3', '1', '4', '1', '5', '1', '6', '0']
def test_filter():
    # Проверка filter().  Получим только единицы.
    filtered_1 = list(filter(lambda x: x == '1', source_data))
    assert len(filtered_1) == 4, f'filtered={filtered_1}'
    assert [x == '1' for x in filtered_1]

    # Проверка filter(). Получим всё кроме единиц.
    filtered_2 = list(filter(lambda x: x != '1', source_data))
    assert len(filtered_2) == 6, f'filtered={filtered_2}'
    assert [x != '1' for x in filtered_2]
    assert [isinstance(x, str) for x in filtered_2], f'filtered={filtered_2}'


def test_map():
    # Проверка map(). Переведем все строки в int.
    mapped_1 = list(map(int, source_data))
    assert len(mapped_1) == len(source_data), f'mapped={mapped_1}'
    assert [isinstance(x, int) for x in mapped_1]


def test_sorted():
    # Проверяем sorted. Сортировка по возрастанию.
    sorted_1 = sorted(source_data)
    assert len(sorted_1) == len(source_data)
    assert [sorted_1[i] <= sorted_1[i+1] for i in range(len(source_data)-1)]

    # Проверяем sorted. Сортировка по убыванию.
    sorted_2 = sorted(source_data, reverse=True)
    assert len(sorted_1) == len(source_data)
    assert [sorted_2[i] >= sorted_2[i+1] for i in range(len(source_data)-1)]


