class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    #     if len(nums) == 1:
    #         return True
            
    #     idx = 0
    #     while idx < len(nums):
    #         if idx == len(nums) - 1:
    #             return True
    #         if nums[idx] == 0:
    #             return False
            
    #         idx += nums[idx]
    #     return False


    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i, num in enumerate(nums):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + num)
        return True
"""
while idx < len(nums)
if nums[idx] == 0
break
idx += nums[idx]
"""
