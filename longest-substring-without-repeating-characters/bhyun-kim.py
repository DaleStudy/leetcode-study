"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Solution: Sliding Window
    - Use a dictionary to store the number of occurrences of each character
    - Use two pointers to traverse the string
    - Increment the right pointer until the substring contains no repeating characters
    - Increment the left pointer until the substring contains repeating characters
    - Update the maximum length of the substring
    - Return the maximum length of the substring

Time complexity: O(n)
    - The time complexity is O(n) because the two pointers traverse the string only once
Space complexity: O(n)
    - Store the number of occurrences of each character in a dictionary
"""

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_count = defaultdict(int)
        right, left = 0, 0
        max_seq = 0
        while right < len(s):
            r = s[right]
            char_count[r] += 1

            while char_count[r] > 1:
                l = s[left]
                char_count[l] -= 1
                left += 1

            max_seq = max(max_seq, right - left + 1)
            right += 1

        return max_seq
