import pytest
from src.animated_parse_tree import ParseTree
from math import pi


@pytest.mark.skip
def test_evaluation(sample_list):
    t = ParseTree()
    t.read(sample_list[0])
    assert t.expression == sample_list[0]
    assert t.evaluate() == sample_list[1]


@pytest.mark.parametrize('sample_list', [
    ['1 + 2 * 3', 7],
    ['20.0 * 41 / 2 ^ 0', 820.0],
    ['5.5 * 2 / 11 + 1.5', 2.5],
    ['20 - 34 * 8 ** 3', -17388],
    ['3 ** 8 * 34 - 20', 223054]
])
def test_infix_operators(sample_list):
    test_evaluation(sample_list=sample_list)


@pytest.mark.parametrize('sample_list', [
    ['0!', 1],
    ['1!', 1],
    ['1 / 0!', 1]
])
def test_postfix_operators(sample_list):
    test_evaluation(sample_list=sample_list)


@pytest.mark.parametrize('sample_list', [
    ['3 * (20 - 5)', 45],
    ['(32 - 16 / (4)) ** 2', 784]
])
def test_parentheses(sample_list):
    test_evaluation(sample_list=sample_list)


@pytest.mark.parametrize('sample_list', [
    ['7(10)', 70],
    ['2pi', 2 * pi],
    ['1 / 2(4)', 0.125]
])
def test_implicit_multiplication(sample_list):
    test_evaluation(sample_list=sample_list)


@pytest.mark.parametrize('sample_list', [
    ['-7.5', -7.5],
    ['54 + -1', 53]
])
def test_unary_operators(sample_list):
    test_evaluation(sample_list=sample_list)
