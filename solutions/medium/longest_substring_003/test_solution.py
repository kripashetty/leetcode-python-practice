"""Test cases for Longest Substring Without Repeating Characters solution.

This module contains test cases for LeetCode #3, including:
- Basic examples from LeetCode
- Edge cases (empty string, single character)
- Special cases (repeating characters, spaces, numbers)
- Complex patterns
"""

from typing import Type

import pytest

from solutions.medium.longest_substring_003.solution import Solution


@pytest.fixture(scope="function")  # type: ignore[misc]
def solution() -> Solution:
    """Fixture that provides a Solution instance."""
    return Solution()


@pytest.mark.parametrize(  # type: ignore[misc]
    "input_string, expected",
    [
        # LeetCode examples
        ("abcabcbb", 3),  # "abc" is longest
        ("bbbbb", 1),  # "b" is longest
        ("pwwkew", 3),  # "wke" is longest
        # Simple cases
        ("a", 1),  # Single character
        ("ab", 2),  # Two different characters
        ("aa", 1),  # Two same characters
        # Complex patterns
        ("dvdf", 3),  # Pattern with repeating character not adjacent
        ("abba", 2),  # Pattern with repeating characters
        ("abcdeafbcd", 6),  # Longer string with multiple patterns
        # Special characters
        ("   ", 1),  # Spaces
        ("123123", 3),  # Numbers
        ("!@#!@#", 3),  # Symbols
        ("a b c", 3),  # Mixed with spaces
        # Long patterns
        ("abcdefghijklmnopqrstuvwxyz", 26),  # All lowercase letters
        ("aA1!bB2@", 8),  # Mixed case, numbers, and symbols
    ],
)
def test_longest_substring(
    solution: Solution, input_string: str, expected: int
) -> None:
    """Test cases for finding longest substring without repeating characters."""
    assert solution.lengthOfLongestSubstring(input_string) == expected


@pytest.mark.parametrize(  # type: ignore[misc]
    "input_string, expected_error",
    [
        ("", ValueError),  # Empty string
    ],
)
def test_longest_substring_error(
    solution: Solution, input_string: str, expected_error: Type[Exception]
) -> None:
    """Test error cases for invalid inputs."""
    with pytest.raises(expected_error):
        solution.lengthOfLongestSubstring(input_string)
