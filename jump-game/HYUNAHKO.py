class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0 
        last_index = len(nums) - 1
        
        for i, jump_len in enumerate(nums):
            if i > max_reachable:
                return False

            max_reachable = max(max_reachable, i + jump_len)
            
            if max_reachable >= last_index:
                return True
                
        return True
