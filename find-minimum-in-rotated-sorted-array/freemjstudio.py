class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_value = 5000
        # O(log n) 이므로 binary search
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            min_value = min(nums[mid], min_value)

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return min_value
