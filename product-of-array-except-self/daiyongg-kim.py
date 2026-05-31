class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)

        #initialize array as 1 
        result = [1] * size

        left_pass = 1

        for i in range(size):A
            result[i] *= left_pass
            left_pass *= nums[i]

        right_pass = 1
        for i in range(size-1, -1, -1):
            result[i] *= right_pass
            right_pass *= nums[i]

        return result
