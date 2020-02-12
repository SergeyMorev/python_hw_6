import math
from math import sqrt, pow

# Тестирование встроенных функций.


def test_pi_identical():
    assert 3.141592653589793 == math.pi


def test_sqrt_1():
    for a in range(0, 10, 1):
        assert math.sqrt(a * a) == a


def test_sqrt_2():
    assert [sqrt(a) * sqrt(a) == a for a in range(0, 10, 1)]


def test_sqrt_constants():
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

    def my_power(a, exp):
        res = 1
        for _ in range(exp):
            res *= a
        return res

    for a in range(5):
        for i in range(0, 11):
            assert pow(a, i) == my_power(a, i)
