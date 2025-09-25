import pytest
from solutions.easy.two_sum_001.solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from LeetCode"""
    # inputs = ...
    # expected = ...
    # assert solution.method_name(*inputs) == expected
    inputs = [2,7,11,15]
    target = 9
    expected = [0,1]
    assert solution.twoSum(inputs, target) == expected

def test_example_2(solution):
    """Test the second example from LeetCode"""
    inputs = [3,2,4]
    target = 6
    expected = [1,2]
    assert solution.twoSum(inputs, target) == expected

def test_example_3(solution):
    """Test the second example from LeetCode"""
    inputs = [3,3]
    target = 6
    expected = [0,1]
    assert solution.twoSum(inputs, target) == expected

def test_edge_cases(solution):
    """Test edge cases for the Two Sum problem"""
    # Empty or small arrays
    assert solution.twoSum([], 5) == []  # Empty array
    assert solution.twoSum([1], 1) == []  # Single element
    assert solution.twoSum([3, 3], 6) == [0, 1]  # Exactly two elements that sum to target
    
    # No solution exists
    assert solution.twoSum([1, 2, 3], 10) == []  # No pair sums to target
    assert solution.twoSum([1, 2, 3], 0) == []  # Target too small
    assert solution.twoSum([1, 2, 3], 100) == []  # Target too large
    
    # Special numbers
    # Test negative numbers (multiple valid solutions: [-1,-4] or [-2,-3])
    result = solution.twoSum([-1, -2, -3, -4], -5)
    nums = [-1, -2, -3, -4]
    assert len(result) == 2  # Should return two indices
    assert result[0] != result[1]  # Indices should be different
    assert 0 <= result[0] < len(nums) and 0 <= result[1] < len(nums)  # Indices should be valid
    assert nums[result[0]] + nums[result[1]] == -5  # Sum should equal target
    assert solution.twoSum([0, 0], 0) == [0, 1]  # Zero values
    assert solution.twoSum([1000000, 1000000], 2000000) == [0, 1]  # Large numbers
    assert solution.twoSum([2, 2, 2, 2], 4) == [0, 1]  # Duplicate numbers

# def test_custom_cases(solution):
#     """Test additional cases with multiple possible solutions"""
#     # Note: The function should return any valid pair
#     result = solution.twoSum([3, 2, 4, 3], 6)  # Multiple valid pairs: [0,3] or [1,2]
#     assert len(result) == 2
#     assert result[0] != result[1]  # Indices should be different
#     assert 0 <= result[0] < 4 and 0 <= result[1] < 4  # Indices should be valid
#     nums = [3, 2, 4, 3]
#     assert nums[result[0]] + nums[result[1]] == 6  # Sum should equal target
