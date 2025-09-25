"""
LeetCode Problem [Number]: [Title]
Difficulty: [Easy/Medium/Hard]
Link: [LeetCode Problem URL]

Time Complexity: O(?)
Space Complexity: O(?)
"""
from typing import List  # Add other type hints as needed


class Solution:
    def twoSum(self, input: List[int], target: int) -> List[int]:
        """
        Args:
            input: List[int]
            target: int
        
        Returns:
            Description of return value
        
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



