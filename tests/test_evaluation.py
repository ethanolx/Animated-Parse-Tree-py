import pytest
from src.animated_parse_tree import ParseTree

@pytest.mark.parametrize('sample_list', [
    ['1 + 2 * 3', 7],
    ['20.0 * 41 / 2 ^ 0', 820.0]
])
def test_evaluation(sample_list):
    t = ParseTree()
    t.read(sample_list[0])
    assert t.expression == sample_list[0]
    assert t.evaluate() == sample_list[1]
