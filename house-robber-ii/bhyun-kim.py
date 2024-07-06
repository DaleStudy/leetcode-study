"""
213. House Robber II
https://leetcode.com/problems/house-robber-ii/

Solution:
    To solve this problem, we can use the dynamic programming approach.
    We can create a helper function to solve the house robber problem for a given range of houses.
    We consider two cases:
        - Rob houses from 0 to n-2.
        - Rob houses from 1 to n-1.
    We return the maximum amount of money that can be robbed from these two cases.

Time complexity: O(n)
    - We iterate through each house once.
    - The helper function has a time complexity of O(n).

Space complexity: O(n)
    - We use a dynamic programming array to store the maximum amount of money that can be robbed.
    - The space complexity is O(n) for the dynamic programming array.

"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses):
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                dp[i] = max(dp[i - 1], houses[i] + dp[i - 2])
            return dp[-1]

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # Case 1: Rob houses from 0 to n-2
        case1 = rob_linear(nums[:-1])
        # Case 2: Rob houses from 1 to n-1
        case2 = rob_linear(nums[1:])

        return max(case1, case2)
