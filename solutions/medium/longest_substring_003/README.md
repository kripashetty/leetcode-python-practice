# 3. Longest Substring Without Repeating Characters

## Problem Description

Given a string `s`, find the length of the longest substring without repeating characters.

### Examples

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

### Constraints

- `0 <= s.length <= 5 * 10⁴`
- `s` consists of English letters, digits, symbols and spaces.

## Solution Approach

### Initial Thoughts
- Need to track characters we've seen to detect repeats
- Can use sliding window technique
- Need to handle empty string case

### Algorithm
1. Use two pointers (start and end) to define the window
2. Use a set/dict to track characters in current window
3. When we find a repeat, shrink window from start
4. Keep track of max length seen so far

Let's say we have the string "abba" and we're trying to find the longest substring without repeating characters:

1. When we start:

    ```
    string:  a  b  b  a

    index:   0  1  2  3

    window:  ^

    seen: {}
    ```

2. After processing 'a' and 'b':

    ```
    string:  a  b  b  a

    index:   0  1  2  3

    window:  ^-----^

    seen: {'a': 0, 'b': 1}
    ```

3. When we hit the second 'b':

   ```
    string:  a  b  b  a

    index:   0  1  2  3

    window:  ^-----^

    seen: {'a': 0, 'b': 1}
   ```


Here's the key part: we see 'b' again at index 2, and we know we saw it before at index 1.

We need to start our new window from index 2 (the position AFTER the first 'b'), not from index 1.

That's why we do seen_characters[character] + 1:

- seen_characters[character] gives us the last position where we saw the character (1 in this case)
- +1 moves us to the next position (2 in this case) to start a fresh window

Without the +1, we would:

- Move the start to index 1 (where we saw 'b')
- Still include the repeating character in our window

With the +1, we:

- Move the start to index 2 (after where we saw 'b')
- Start a fresh window that doesn't include the repeating character

Here's another example with "abcabcbb":



When we hit second 'a':

```
string:  a  b  c  a  b  c  b  b

index:   0  1  2  3  4  5  6  7

^--------^

seen['a'] = 0
```

We want to start new window from index 1 (0 + 1)


to get: 

```
a  b  c  a  b  c  b  b

0  1  2  3  4  5  6  7

^--------^

```

The +1 ensures we:

1. Skip past the last occurrence of the repeated character
2. Start a fresh window with no repeating characters
3. Don't include the character we just found a repeat of


### Complexity Analysis
- Time Complexity: O(n) where n is length of string
- Space Complexity: O(min(m,n)) where m is size of character set
- Operations are linear as window only moves formward and each index is visited only once




## Test Cases

### Edge Cases
- Empty string
- Single character
- All same characters
- No repeating characters

### Special Cases
- String with spaces
- String with special characters
- String with numbers
- Very long string

### Example Cases
From LeetCode:
1. "abcabcbb" -> 3
2. "bbbbb" -> 1
3. "pwwkew" -> 3
