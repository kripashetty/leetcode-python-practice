"""Test cases for the Two Sum solution.

This module contains test cases for the Two Sum problem, including:
- Basic examples from LeetCode
- Edge cases (empty arrays, single elements)
- Error cases (no solution exists)
- Special number cases (zeros, large numbers, duplicates)
- Multiple solution cases
"""

from typing import List

import pytest

from solutions.easy.two_sum_001.solution import Solution


@pytest.fixture(scope="function")  # type: ignore[misc]
def solution() -> Solution:
    """Fixture that provides a Solution instance."""
    return Solution()


@pytest.mark.parametrize(  # type: ignore[misc]
    "nums, target, expected",
    [
        # LeetCode example cases
        ([2, 7, 11, 15], 9, [0, 1]),  # Example 1
        ([3, 2, 4], 6, [1, 2]),  # Example 2
        ([3, 3], 6, [0, 1]),  # Example 3
    ],
)
def test_examples(
    solution: Solution, nums: List[int], target: int, expected: List[int]
) -> None:
    """Test the example cases from LeetCode."""
    assert solution.twoSum(nums, target) == expected


@pytest.mark.parametrize(  # type: ignore[misc]
    "nums, target, expected",
    [
        # Valid cases
        ([3, 3], 6, [0, 1]),  # Exactly two elements that sum to target
    ],
)
def test_valid_edge_cases(
    solution: Solution, nums: List[int], target: int, expected: List[int]
) -> None:
    """Test edge cases that should return valid results."""
    assert solution.twoSum(nums, target) == expected


@pytest.mark.parametrize(  # type: ignore[misc]
    "nums, target, reason",
    [
        # Empty or invalid arrays
        ([], 5, "Empty array - can't form a pair"),
        ([1], 1, "Single element - can't form a pair"),
        # No solution exists
        ([1, 2, 3], 10, "No pair sums to target"),
        ([1, 2, 3], 0, "No pair sums to target"),
        ([1, 2, 3], 100, "No pair sums to target"),
    ],
)
def test_error_edge_cases(
    solution: Solution, nums: List[int], target: int, reason: str
) -> None:
    """Test edge cases that should raise ValueError."""
    with pytest.raises(ValueError, match=reason):
        solution.twoSum(nums, target)


@pytest.mark.parametrize(  # type: ignore[misc]
    "nums, target, expected",
    [
        # Special number cases
        ([0, 0], 0, [0, 1]),  # Zero values
        ([1000000, 1000000], 2000000, [0, 1]),  # Large numbers
        ([2, 2, 2, 2], 4, [0, 1]),  # Duplicate numbers
    ],
)
def test_special_numbers(
    solution: Solution, nums: List[int], target: int, expected: List[int]
) -> None:
    """Test cases with special numbers (zeros, large numbers, duplicates)."""
    assert solution.twoSum(nums, target) == expected


def test_multiple_solutions(solution: Solution) -> None:
    """Test cases where multiple valid solutions exist."""
    # Test negative numbers (multiple valid solutions: [-1,-4] or [-2,-3])
    nums = [-1, -2, -3, -4]
    target = -5
    result = solution.twoSum(nums, target)

    # Verify the solution properties
    assert len(result) == 2, "Should return exactly two indices"
    assert result[0] != result[1], "Indices should be different"
    assert all(0 <= i < len(nums) for i in result), "Indices should be valid"
    assert nums[result[0]] + nums[result[1]] == target, "Sum should equal target"
