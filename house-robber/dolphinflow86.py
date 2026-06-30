# Solved using a top down dp (memoization) approach.
# TC: O(N) where N = len(nums) - Each house is visited at most once due to caching.
# SC: O(N) where N = len(nums) - Used for the memoization dictionary and recursion call stack.
class Solution:
    def rec(self, house: int, nums: List[int], memo: Dict[int,int]) -> int:
        if house >= len(nums): return 0
        
        if house in memo: return memo[house]

        # max between (robbing current house + skipping next) or (skipping current house)
        current_robbed = max(nums[house] + self.rec(house + 2, nums, memo), self.rec(house + 1, nums, memo))
        memo[house] = current_robbed
        return current_robbed
        
    def rob(self, nums: List[int]) -> int:
        memo: Dict[int,int] = {}
        return self.rec(0, nums, memo)
