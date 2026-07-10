"""
Time Complexity: O(log N)
Space Complexity: O(1)

### Binary Search Solution ###

1. Initialize two pointers, left and right, to the start and end of the array
2. While left is less than right, calculate the middle index
3. If nums[mid] > nums[right], search the right half (left = mid + 1)
  - Why? mid is in the left sorted portion (larger values), so the rotation point (minimum) must be to the right of mid
4. Otherwise, search the left half including mid (right = mid)
  - nums[mid] <= nums[right] means mid is in the right sorted portion or the array is not rotated, so the minimum is at mid or to its left
5. When left == right, return nums[right]
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, N - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[right]

"""
Time Complexity: O(N)
Space Complexity: O(1)

### Linear Search Solution ### ( NOT RECOMMENDED )

1. Return the minimum element in the array
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
