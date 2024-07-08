"""
198. House Robber
https://leetcode.com/problems/house-robber/

Solution:
    To solve this problem, we can use the dynamic programming approach.
    We can create a dynamic programming array to store the maximum amount of money that can be robbed.
    We consider two cases:
        - Rob the current house and the house two steps back.
        - Skip the current house and rob the house one step back.
    We return the maximum amount of money that can be robbed from these two cases.

Time complexity: O(n)
    - We iterate through each house once.
    - The dynamic programming array has a time complexity of O(n).

Space complexity: O(n)
    - We use a dynamic programming array to store the maximum amount of money that can be robbed.
    - The space complexity is O(n) for the dynamic programming array.
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]
