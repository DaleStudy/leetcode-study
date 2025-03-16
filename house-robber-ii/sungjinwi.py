"""
    풀이 : 
        start를 포함하는 경우와 end를 포함하는 경우를 나눠서 dp 진행

    nums의 갯수 N

    TC : O(N)

    SC : O(1)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prv1, cur1 = 0, 0
        prv2, cur2 = 0, 0
        for i in range(1, len(nums)):
            prv1, cur1 = cur1, max(cur1, prv1 + nums[i])
        for i in range(len(nums) - 1):
            prv2, cur2 = cur2, max(cur2, prv2 + nums[i])
        return max(cur1, cur2)
