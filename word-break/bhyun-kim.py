"""
139. Word Break
https://leetcode.com/problems/word-break/

Solution: 
    This problem can be solved using a recursive approach with memoization.
    We can define a recursive function that takes an index as an argument.
    The function checks if the substring from the current index to the end of the string can be broken into words from the dictionary.
    We can use memoization to store the results of subproblems to avoid redundant calculations.

    - Define a recursive function that takes an index as an argument.
    - Check if the substring from the current index to the end of the string can be broken into words from the dictionary.
    - Use memoization to store the results of subproblems.
    - Return the result of the recursive function.

Time complexity: O(n*m*k)
    - n is the length of the input string.
    - m is the number of words in the dictionary.
    - k is the average length of the words in the dictionary
    - The time complexity is O(n*m*k) due to the nested loops.

Space complexity: O(n)
    - We use memoization to store the results of subproblems.
    - The space complexity is O(n) to store the results of subproblems.
"""

from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i):
            if i < 0:
                return True

            for word in wordDict:
                if s[i - len(word) + 1 : i + 1] == word and dp(i - len(word)):
                    return True

            return False

        return dp(len(s) - 1)
