# O(n) times, O(n) spaces
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_keys = dict.fromkeys(nums,0)
        last = 0
        
        for i in range(len(nums)):
            if not i in nums_keys:
                return i
            last += 1
        
        return last
