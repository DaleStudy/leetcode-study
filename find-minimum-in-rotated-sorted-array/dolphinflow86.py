# 1) Use binary search to halves to search range. Each iteration, 
# compare with nums[pivot] and nums[right] to see which side has a smaller range. 
# Firstly I compare nums[left] with nums[right] so I got the wrong results but end up with the right solution.
# TC: O(logN) where N is the length of the nums array
# SC: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[right]
