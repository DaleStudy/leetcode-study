# O(n) times, O(n) spaces
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_keys = set(nums)
        
        for i in range(len(nums)):
            if not i in nums_keys:
                return i
        
        return len(nums)
