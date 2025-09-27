"""Solution for Longest Substring Without Repeating Characters.

LeetCode Problem 3. Longest Substring Without Repeating Characters
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Time: O(n) where n is the length of the string
Space: O(min(m,n)) where m is the size of the character set
"""

from typing import Dict


class Solution:
    """Solution class for the Longest Substring Without Repeating Characters."""

    def lengthOfLongestSubstring(self, input_string: str) -> int:
        """Find the length of the longest substring without repeating characters.

        Uses sliding window technique with a dictionary to track character positions.
        Maintains a window that grows until a repeat is found, then shrinks from start.

        Args:
            input_string: The input string to process.

        Returns:
            The length of the longest substring without repeating characters.

        Examples:
            >>> Solution().lengthOfLongestSubstring("abcabcbb")
            3
            >>> Solution().lengthOfLongestSubstring("bbbbb")
            1
            >>> Solution().lengthOfLongestSubstring("pwwkew")
            3
        """
        if len(input_string) == 0:
            raise ValueError("Empty string - can't find longest substring")

        seen_characters: Dict[str, int] = {}  # Maps character -> last seen index
        max_length = 0
        start_index = 0

        for end_index, character in enumerate(input_string):
            if character in seen_characters:
                start_index = max(start_index, seen_characters[character] + 1)
            seen_characters[character] = end_index
            max_length = max(max_length, end_index - start_index + 1)
        return max_length
