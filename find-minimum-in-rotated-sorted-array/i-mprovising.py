"""
Time complexity O(logn)
Space compexity O(1)

Binary search
"""

class Solution:

    def findMin(self, nums: List[int]) -> int:
        start = 1
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[0] < nums[mid]:
                start = mid + 1
            else:
                end = mid - 1 

        return nums[0]
