# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/

"""
문제:
    - 집들이 원형으로 배치되어 있고, 각 집에는 돈이 들어 있다.
    - 인접한 두 집은 같은 날 털 수 없다.
    - 첫 집과 마지막 집도 인접한 것으로 본다.
    - 털 수 있는 최대 금액을 구한다.

복잡도:
    n: `nums`의 길이
    Time: O(n)
    Space: O(1)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def steel(start, end):
            prev2, prev1 = 0, 0
            for i in range(start, end):
                cur = max(prev2 + nums[i], prev1)
                prev2, prev1 = prev1, cur
            return prev1

        s1 = steel(0, n - 1)
        s2 = steel(1, n)
        return max(s1, s2)
