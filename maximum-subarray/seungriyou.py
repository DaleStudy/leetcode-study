# https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)

        [Approach]
            dp[i] = nums[i]까지 봤을 때, (1) nums[i]가 포함되면서 (2) 가장 sum이 큰 subarray의 sum 값
                  = max(dp[i - 1] + num, num)
        """

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = nums[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_sum = max(max_sum, dp[i])

        return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            space optimized DP
        """

        prev = max_sum = nums[0]

        for i in range(1, len(nums)):
            prev = max(prev + nums[i], nums[i])
            max_sum = max(max_sum, prev)

        return max_sum
