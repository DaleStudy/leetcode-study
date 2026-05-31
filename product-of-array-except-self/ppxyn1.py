# idea: O(n) - There is no multiplication calculate it as O(1) / addition is possible

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length
        
        prefix,suffix = 1,1
        for i in range(length):       
            answer[i] = prefix
            prefix *= nums[i]
        for j in range(length - 1, -1, -1):  
            answer[j] *= suffix
            suffix *= nums[j]
        return answer
    

