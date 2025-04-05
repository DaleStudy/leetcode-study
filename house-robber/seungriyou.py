# https://leetcode.com/problems/house-robber/

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1) (space-optimized DP)

        [Approach]
            인접한 두 집을 모두 털면 안 되므로 다음과 같이 dp table을 구상할 수 있다.
                dp[i] = (순차적으로) i-th house를 털 때 얻을 수 있는 max amount of money
                      = max(이전 집을 털었을 때, 이전 집을 털지 않았을 때)
                      = max(지금 집을 털 수 없을 때, 지금 집을 털 수 있을 때)
                      = max(dp[i - 1], dp[i - 2] + nums[i])
            이때, dp[i] 값을 채우기 위해 dp[i - 1]과 dp[i - 2] 값만 필요하므로,
            O(n) space(= list)가 아닌 O(1) space(= variables)로 optimize 할 수 있다.
                prev1 = dp[i - 1]
                prev2 = dp[i - 2]
        """

        prev1 = prev2 = 0

        for num in nums:
            prev1, prev2 = max(prev1, prev2 + num), prev1  # -- multiple assignment

        return prev1
