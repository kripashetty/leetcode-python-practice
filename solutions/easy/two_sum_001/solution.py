"""Two Sum solution implementation.

LeetCode Problem 1: Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

Time: O(n) on average; O(1) best case (pair found immediately);
O(n²) in a theoretical worst case if hash
lookups/insertions degrade due to adversarial collisions.

Space: O(n) extra (the seen_nums dict can grow to ~n entries).
"""


class Solution:
    """Solution class for the Two Sum problem."""

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Find two numbers in the array that add up to the target.

        Args:
            nums: List of integers to search through
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
        # Inefficient
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # Efficient
        if len(nums) < 2:
            reason = (
                "Empty array - can't form a pair"
                if not nums
                else "Single element - can't form a pair"
            )
            raise ValueError(reason)
        seen_nums: dict[int, int] = {}  # type-annotated empty dict
        for idx, num in enumerate(nums):
            if target - num in seen_nums:
                return [seen_nums[target - num], idx]
            seen_nums[num] = idx

        raise ValueError("No pair sums to target")
