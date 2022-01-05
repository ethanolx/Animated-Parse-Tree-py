import pytest
from src.animated_parse_tree import ParseTree


@pytest.mark.skip
def test_evaluation(sample_list, parse_tree):
    parse_tree.read(sample_list[0])
    assert parse_tree.expression == sample_list[0]
    assert parse_tree.evaluate() == sample_list[1]


@pytest.fixture
def epochs():
    return 100


@pytest.fixture
def parse_tree():
    return ParseTree()
