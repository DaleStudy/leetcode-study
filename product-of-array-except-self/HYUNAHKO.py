class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result_list = [0] * n
        if len(nums) <2 or len(nums) > 1e5:
            return None 
        
        p = 1
        for i in range(n):
            result_list[i] = p
            p *= nums[i] 
            
        p = 1
        for i in range(n - 1, -1, -1): 
            result_list[i] *= p
            p *= nums[i] 
            
        return result_list
   