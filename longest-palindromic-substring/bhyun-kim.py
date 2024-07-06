"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Solution:
    To solve this problem, we can use the expand from center approach.
    We can iterate through each character in the string and expand around it to find palindromes.
    We handle both odd-length and even-length palindromes by checking two cases.
    We return the longest palindrome found.

Time complexity: O(n^2)
    - We iterate through each character in the string.
    - For each character, we expand around it to find palindromes.

Space complexity: O(1)
    - We use constant space to store the maximum palindrome found.

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str
