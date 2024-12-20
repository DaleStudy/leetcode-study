# FIRST WEEK

# Question : 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
# removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# Notes:
# Using `reverse`(O(N)) api and matching all(max O(N)) look straightforward.
# The two pointer method may useful to decrease time complexity.
# If length of input is 0 or 1, return true.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        if l < 2:
            return True

        f = 0
        b = l - 1

        while (f <= b):
            if (s[f] == " " or (s[f].isalpha() == False and s[f].isnumeric() == False)):
                f = f + 1
                continue

            if (s[b] == " " or (s[b].isalpha() == False and s[b].isnumeric() == False)):
                b = b - 1
                continue

            if s[f].lower() != s[b].lower():
                return False

            f = f + 1
            b = b - 1

        return True
