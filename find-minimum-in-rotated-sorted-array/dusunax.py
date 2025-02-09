'''
# 153. Find Minimum in Rotated Sorted Array

> **why binary search works in a "rotated" sorted array?**  
> rotated sorted array consists of **two sorted subarrays**, and the minimum value is the second sorted subarray's first element.  
> so 👉 find the point that second sorted subarray starts.   
>
> - if nums[mid] > nums[right]? => the pivot point is in the right half.  
> - if nums[mid] <= nums[right]? => the pivot point is in the left half.  
> - loop until left and right are the same.
'''
class Solution:
    '''
    ## A. brute force(not a solution)
    - TC: O(n)
    - SC: O(1)
    '''
    def findMinBF(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return min(nums) # check all elements

    '''
    ## B. binary search
    - TC: O(log n)
    - SC: O(1)
    '''
    def findMinBS(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
