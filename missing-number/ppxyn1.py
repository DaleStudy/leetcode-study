# idea : - 
# Time Complexity : below O(n^2)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()      
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
    

