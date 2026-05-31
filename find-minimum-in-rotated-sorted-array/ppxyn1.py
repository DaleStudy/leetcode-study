class Solution:
    def findMin(self, nums: List[int]) -> int:
        # You must write an algorithm that runs in O(log n) time. >> Binary Search 
        # It's possible because the array is sorted.        
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            # If the value at mid is greater than the value at the right end, it means the minimum place to the right of mid.
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # mid can be minimum number
                # But is it possible to solve it with "right=mid-1"? e.g,[4,5,6,7,0,1,2]
                right = mid
        return nums[left]



