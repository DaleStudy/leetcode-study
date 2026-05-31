

#33. Search in Rotated Sorted Array
# First Try: use binary search but consider the rotated part

# Solution: Find the minimum index where the rotation happens, then do binary search in the appropriate half.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        # 1. find the index of the smallest value using binary search.
        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        min_i = l
        # 2. determine which part to do binary search on.
        # First edge case: if the smallest index is 0, meaning the array is not rotated.
        if min_i == 0:
            l, r = 0, n - 1
        # Second edge case: if the target is the left part
        elif target >= nums[0] and target <= nums[min_i - 1]:
            l, r = 0, min_i - 1
        # Third edge case: if the target is the right part
        else:
            l, r = min_i, n - 1
        # 3. do binary search on the determined part.
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

# Time Complexity: O(log(n))
# Space Complexity: O(1)
        # if target not in nums:
        #     return -1

        # # two cases: 
        # # 1. [left side], [right side]
        # # if we figure out where is the boundary then we can just use binary search 
        
        # def bst(target, start, end):
        #     if ( start > end):
        #         return -1
        
        #     mid = math.floor((end + start) / 2)
        #     print(nums[mid])
        #     # 1. right side - sorted array 

        #     if nums[mid] == target:
        #         return mid 
        #     elif ( nums[mid] < target) and nums[start] < nums[end]:
        #         return bst(target, mid+1, end)
        #     elif ( nums[mid] > target) and  nums[start] < nums[end]:
        #         return bst(target, start, mid -1)
        #     elif ( nums[mid] < target) and nums[start] > nums[end]:
        #         return bst(target, start, mid -1)
        #     elif ( nums[mid] > target) and nums[start] > nums[end]:
        #         return bst(target, mid+1, end)
        # return bst(target, 0, len(nums) -1)

