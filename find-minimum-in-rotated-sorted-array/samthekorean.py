class Solution:
    # TC: O(log(n)) - The search space is halved each round until the minimum is found
    # SC: O(1) - Only a few extra variables are used regardless of input size
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (high + low) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]
