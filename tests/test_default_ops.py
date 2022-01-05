from math import acos, acosh, asin, asinh, atan, atanh, cos, factorial, log, log10, pi, sin, sqrt, tan
import pytest
from src.animated_parse_tree.utils.custom_functions import double_factorial, hyperfactorial, superfactorial, tetrate
from src.animated_parse_tree import ParseTree
from random import randint, random



@pytest.mark.parametrize('sample_list', [
    ['-{', lambda a: -a, (0, 100)],
    ['{++', lambda a: a + 1],
    ['{--', lambda a: a - 1],
    ['abs {', abs, (-100, 100)],
    ['modulus {', abs, (-100, 100)],
    ['_/{', sqrt],
    ['lg {', log10, (1, 100)],
    ['ln {', log, (1, 100)],
    ['{ deg', lambda a: (pi / 180) * a],
    ['{ degrees', lambda a: (pi / 180) * a],
    ['sin {', sin],
    ['sine {', sin],
    ['cos {', cos],
    ['cosine {', cos],
    ['tan {', lambda a: tan(a)],
    ['tangent {', lambda a: tan(a)],
    ['csc {', lambda a: 1 / sin(a), (-3, 3)],
    ['sec {', lambda a: 1 / cos(a), (-3, 3)],
    ['cot {', lambda a: 1 / tan(a), (-3, 3)],
    ['asin {', lambda a: asin(a), (-1, 1)],
    ['acos {', lambda a: acos(a), (-1, 1)],
    ['atan {', lambda a: atan(a), (-1, 1)],
    ['asinh {', lambda a: asinh(a)],
    ['acosh {', lambda a: acosh(a)],
    ['atanh {', lambda a: atanh(a)],
    ['{!', factorial, (0, 20)],
    ['{!!', double_factorial, (0, 30)],
    ['{$', superfactorial, (0, 10)],
    ['{#', hyperfactorial, (0, 5)],
    ['~{', lambda a: 1 if a == 0 else 0, (0, 1)],
    ['not {', lambda a: 1 if a == 0 else 0, (0, 1)]
])
def test_unary_operators(sample_list, epochs, parse_tree):
    min_a = 0
    max_a = 100
    if len(sample_list) == 3:
        min_a, max_a = sample_list[2]
    for _ in range(epochs):
        try:
            a = randint(min_a, max_a)
            parse_tree.read(sample_list[0].replace('{', str(a)))
            assert parse_tree.evaluate() == sample_list[1](a)
        except ZeroDivisionError:
            pass
        except ValueError as e:
            if str(e) != 'math domain error':
                raise e

@pytest.mark.parametrize('sample_list', [
    ['{ + }', lambda a, b: a + b],
    ['{ - }', lambda a, b: a - b],
    ['{ * }', lambda a, b: a * b],
    ['{ / }', lambda a, b: a / b, (0, 100, 1, 100)],
    ['{ // }', lambda a, b: a // b, (0, 100, 1, 100)],
    ['{ % }', lambda a, b: a % b, (0, 100, 1, 100)],
    ['{ mod }', lambda a, b: a % b, (0, 100, 1, 100)],
    ['{ modulo }', lambda a, b: a % b, (0, 100, 1, 100)],
    ['{ ^ }', lambda a, b: a ** b],
    ['{ ** }', lambda a, b: a ** b],
    ['{ _/ }', lambda a, b: b ** (1 / a), (1, 100, 0, 100)],
    ['log({, })', lambda a, b: log(b, a), (2, 100, 1, 100)],
    ['{ ^^ }', lambda a, b: tetrate(a, b), (0, 12, 0, 2)],
    ['{ | }', lambda a, b: 1 if a == 1 or b == 1 else 0, (0, 1, 0, 1)],
    ['{ || }', lambda a, b: 1 if a == 1 or b == 1 else 0, (0, 1, 0, 1)],
    ['{ or }', lambda a, b: 1 if a == 1 or b == 1 else 0, (0, 1, 0, 1)],
    ['{ xor }', lambda a, b: 1 if (a == 1 and b == 0) or (a == 0 and b == 1) else 0, (0, 1, 0, 1)],
    ['{ & }', lambda a, b: 1 if a == 1 and b == 1 else 0, (0, 1, 0, 1)],
    ['{ && }', lambda a, b: 1 if a == 1 and b == 1 else 0, (0, 1, 0, 1)],
    ['{ and }', lambda a, b: 1 if a == 1 and b == 1 else 0, (0, 1, 0, 1)],
    ['{ < }', lambda a, b: int(a < b)],
    ['{ <= }', lambda a, b: int(a <= b)],
    ['{ > }', lambda a, b: int(a > b)],
    ['{ >= }', lambda a, b: int(a >= b)],
    ['{ = }', lambda a, b: int(a == b)],
    ['{ == }', lambda a, b: int(a == b)],
    ['{ <> }', lambda a, b: int(a != b)],
    ['{ != }', lambda a, b: int(a != b)]
])
def test_binary_operators(sample_list, epochs, parse_tree):
    min_a = min_b = 0
    max_a = max_b = 100
    if len(sample_list) == 3:
        min_a, max_a, min_b, max_b = sample_list[2]
    for _ in range(epochs):
        try:
            a = randint(min_a, max_a)
            b = randint(min_b, max_b)
            parse_tree.read(sample_list[0].replace('{', str(a)).replace('}', str(b)))
            assert parse_tree.evaluate() == sample_list[1](a, b)
        except ValueError as e:
            if str(e) != 'math domain error':
                raise e
