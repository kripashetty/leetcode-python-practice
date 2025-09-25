import pytest
from .solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from LeetCode"""
    # inputs = ...
    # expected = ...
    # assert solution.method_name(*inputs) == expected
    pass

def test_example_2(solution):
    """Test the second example from LeetCode"""
    pass

def test_edge_cases(solution):
    """Test edge cases"""
    pass

def test_custom_cases(solution):
    """Test additional custom cases"""
    pass
