"""
300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

Solution:
    To solve this problem, we can use the dynamic programming approach.
    We create a list to store the longest increasing subsequence ending at each index.
    We iterate through the array and update the longest increasing subsequence ending at each index.
    We return the maximum length of the longest increasing subsequence.

Time complexity: O(n log n)
    - We iterate through each element in the array once.
    - We use the bisect_left function to find the position to insert the element in the sub list.
    - The time complexity is O(n log n) for inserting elements in the sub list.

Space complexity: O(n)
    - We use a list to store the longest increasing subsequence ending at each index.
"""

from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            pos = bisect_left(sub, num)
            if pos < len(sub):
                sub[pos] = num
            else:
                sub.append(num)
        return len(sub)
