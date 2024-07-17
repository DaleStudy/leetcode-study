"""
647. Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/

Solution:
    To solve this problem, we can use the expand from center technique.
    We can iterate through each character in the string and expand from the center to find palindromic substrings.
    We can handle both odd and even length palindromes by expanding from the center and center + 1.
    We keep track of the number of palindromic substrings found.
    The total number of palindromic substrings is the sum of palindromic substrings found at each character.

Time complexity: O(n^2)
    - We iterate through each character in the string.
    - For each character, we expand from the center to find palindromic substrings.
    - The time complexity is O(n^2) due to the nested loops.

Space complexity: O(1)
    - We use constant space to store variables.
    - The space complexity is O(1).
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        num_pal_strs = 0

        def expand_from_center(left, right):
            num_pal = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                num_pal += 1
            return num_pal

        for i in range(len(s)):
            num_pal_strs += expand_from_center(i, i)
            num_pal_strs += expand_from_center(i, i + 1)

        return num_pal_strs
