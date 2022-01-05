import pytest
from math import pi
from conftest import test_evaluation


@pytest.mark.parametrize('sample_list', [
    ['1 + 2 * 3', 7],
    ['20.0 * 41 / 2 ^ 0', 820.0],
    ['5.5 * 2 / 11 + 1.5', 2.5],
    ['20 - 34 * 8 ** 3', -17388],
    ['3 ** 8 * 34 - 20', 223054]
])
def test_infix_operators(sample_list, parse_tree):
    test_evaluation(sample_list=sample_list, parse_tree=parse_tree)


@pytest.mark.parametrize('sample_list', [
    ['0!', 1],
    ['1!', 1],
    ['1 / 0!', 1]
])
def test_postfix_operators(sample_list, parse_tree):
    test_evaluation(sample_list=sample_list, parse_tree=parse_tree)


@pytest.mark.parametrize('sample_list', [
    ['3 * (20 - 5)', 45],
    ['(32 - 16 / (4)) ** 2', 784]
])
def test_parentheses(sample_list, parse_tree):
    test_evaluation(sample_list=sample_list, parse_tree=parse_tree)


@pytest.mark.parametrize('sample_list', [
    ['7(10)', 70],
    ['2pi', 2 * pi],
    ['1 / 2(4)', 0.125]
])
def test_implicit_multiplication(sample_list, parse_tree):
    test_evaluation(sample_list=sample_list, parse_tree=parse_tree)


@pytest.mark.parametrize('sample_list', [
    ['-7.5', -7.5],
    ['54 + -1', 53]
])
def test_unary_operators(sample_list, parse_tree):
    test_evaluation(sample_list=sample_list, parse_tree=parse_tree)
