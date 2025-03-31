# Time Complexity: O(log n) - using binary search, so cut the search space in half each time.
# Space Complexity: O(1) - only use a few variables (low, high, mid), no extra space.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        # start with the full range of the array
        high = len(nums) - 1  

        # find the middle index
        while low < high:
            mid = low + (high - low) // 2  

            # if mid is greater than the last element, the min must be on the right
            if nums[mid] > nums[high]:
                # move the low pointer to the right
                low = mid + 1  
            else:
                # min could be mid or in the left part
                high = mid  
        # low and high converge to the minimum element
        return nums[low]
