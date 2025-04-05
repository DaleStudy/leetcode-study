class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        
        nums = sorted(set(nums))
        
        currLength = 1
        lastNum = nums[0]
        result = 1
        
        for i in range(1, len(nums)):
            if nums[i] == lastNum + 1:
                currLength += 1
            else:
                currLength = 1
            
            result = max(result, currLength)
            lastNum = nums[i]
        
        return result 

    
    