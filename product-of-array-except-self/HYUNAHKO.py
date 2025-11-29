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
        
    

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_list = [0] * len(nums)
        if len(nums) <2 or len(nums) > 1e5:
            return None 
        
        for idx in range(0, len(nums)):
            result = 1
            for idx_left in range(0, idx):
                result *= nums[idx_left]

            for idx_right in range(idx+1, len(nums)):
                result *= nums[idx_right]
            
            result_list[idx] = result


        return result_list
        