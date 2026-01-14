class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = 0
        for i in range(len(nums)):
            if max_pos < i:
                return False
            if i+nums[i] > max_pos:
                max_pos = i+nums[i]
        return True
    
