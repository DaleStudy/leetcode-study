"""
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

Solution: Sliding Window
    - Use a dictionary to store the number of occurrences of each character
    - Use two pointers to traverse the string
    - Increment the right pointer until the substring contains no repeating characters
    - Increment the left pointer until the substring contains repeating characters
        To do this, 
            - Find the maximum frequency of the characters in the substring
            - If the length of the substring minus the maximum frequency is greater than k, increment the left pointer
    - Update the maximum length of the substring
    - Return the maximum length of the substring

Time complexity: O(n)
    - The time complexity is O(n) because the two pointers traverse the string only once

Space complexity: O(n)
    - Store the number of occurrences of each character in a dictionary
"""


from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        left, right = 0, 0
        max_seq = 1
        max_freq = 0

        while right < len(s):
            r = s[right]
            char_freq[r] += 1

            max_freq = 0
            for v in char_freq.values():
                max_freq = max(v, max_freq)

            while right - left + 1 - max_freq > k and left < right:
                l = s[left]
                char_freq[l] -= 1
                left += 1

                max_freq = 0
                for v in char_freq.values():
                    max_freq = max(v, max_freq)

            max_seq = max(right - left + 1, max_seq)
            right += 1

        return max_seq
