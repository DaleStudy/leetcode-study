# Time Complexity: O(log n) - using a modified binary search, 
# Space Complexity: O(1) - no extra space used, just a few variables.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # default result, in case the target isn't found
        res = -1  
         # set up the binary search range
        left, right = 0, len(nums) - 1 

        while left <= right:
            # calculate the middle index
            mid = left + (right - left) // 2 
            
            # found the target, store the index
            if nums[mid] == target:  
                res = mid
            
            # check if the left half is sorted
            if nums[left] <= nums[mid]:  
                if nums[left] <= target < nums[mid]:  
                    # target in the left half, move right pointer
                    right = mid - 1  
                else: 
                    # otherwise, search in the right half
                    left = mid + 1 
            
            # otherwise, the right half must be sorted
            else:  
                if nums[mid] < target <= nums[right]:  
                    # target in the right half, move left pointer
                    left = mid + 1 
                else: 
                    # otherwise, search in the left half
                    right = mid - 1 

        return res 
