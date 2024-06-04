"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/

Solution:
    - Create a set of the input list
    - Iterate through the set
    - For each element, find the consecutive elements
    - Use a while loop to find the consecutive elements
    - Update the longest length

Time complexity: O(n)
    - O(n) for iterating through the set

Space complexity: O(n)
    - O(n) for the set
    - Total: O(n)

"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_len = 0
        nums_set = set(nums)

        for n in nums_set:
            if n - 1 not in nums_set:
                current_n = n
                current_len = 1

                while current_n + 1 in nums_set:
                    current_n += 1
                    current_len += 1

                longest_len = max(longest_len, current_len)

        return longest_len
