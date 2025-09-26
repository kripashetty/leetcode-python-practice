"""Two Sum solution implementation.

LeetCode Problem 1: Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

Time Complexity: O(n²)
Space Complexity: O(1)
"""

from typing import List  # Add other type hints as needed


class Solution:
    """Solution class for the Two Sum problem."""

    def twoSum(self, input: List[int], target: int) -> List[int]:
        """Find two numbers in the array that add up to the target.

        Args:
            input: List of integers to search through
            target: The target sum to find

        Returns:
            A list containing the indices of the two numbers that sum to target.
            Returns empty list if no solution exists.

        Examples:
            >>> Solution().twoSum([2,7,11,15], 9)
            [0, 1]
            >>> Solution().twoSum([3,2,4], 6)
            [1, 2]
            >>> Solution().twoSum([3,3], 6)
            [0, 1]
        """
        # Your solution here
        for i in range(len(input)):
            for j in range(i + 1, len(input)):
                if input[i] + input[j] == target:
                    return [i, j]
        return []
