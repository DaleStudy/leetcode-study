"""
시간 복잡도 O(N)
공간 복잡도 O(N)


"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def backtracking(k: int) -> int:
            if k >= len(nums):
                return 0
            if k in memo:
                return memo[k]
            
            rob = nums[k] + backtracking(k + 2)
            skip = backtracking(k + 1)

            memo[k] = max(rob, skip)
            return memo[k]
        
        return backtracking(0)
