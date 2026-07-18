# TC: O(logN)
# SC: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high - 1:
            mid = (low + high) // 2

            if nums[low] < nums[mid] < nums[high]:
                return nums[low]

            if nums[low] > nums[mid]:
                high = mid
            else:
                low = mid + 1

        return min(nums[low], nums[high])

