'''
TC : O(n)
SC : O(1)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dp(start, end):
            prv, cur = 0, 0
            for idx in range(start, end):
                prv, cur = cur, max(prv + nums[idx], cur)
            return cur
        return max(dp(1, len(nums)), dp(0, len(nums) - 1))
