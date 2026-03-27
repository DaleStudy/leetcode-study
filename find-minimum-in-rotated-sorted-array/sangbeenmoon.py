# TC : O(logN)
# SC : 1

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        if len(nums) == 2:
            return min(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid
            
        return min(nums[left], nums[right], nums[mid])
