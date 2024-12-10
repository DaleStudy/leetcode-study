class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def getAmount(start: int) -> int:
            if not start < len(nums):
                memo[start] = 0
            if start in memo:
                return memo[start]

            memo[start] = max(nums[start] + getAmount(start+2), getAmount(start+1))

            return memo[start]
        
        return getAmount(0)

