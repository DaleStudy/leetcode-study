class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary Search: compare mid with right
        # nums[mid] > nums[right] -> min is in right half
        # nums[mid] < nums[right] -> min is in left half (including mid)

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid

        return nums[left]

# Time Complexity: O(log n)
# Space Complexity: O(1)
