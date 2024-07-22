"""
55. Jump Game
https://leetcode.com/problems/jump-game/

Solution:
    To solve this problem, we can use the greedy approach.
    We iterate through the array and keep track of the maximum index we can reach.
    If the current index is greater than the maximum index we can reach, we return False.
    Otherwise, we update the maximum index we can reach.
    If we reach the end of the array, we return True.

Time complexity: O(n)
    - We iterate through each element in the array once.

Space complexity: O(1)
    - We use a constant amount of extra space.
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
        return max_reach >= len(nums) - 1
