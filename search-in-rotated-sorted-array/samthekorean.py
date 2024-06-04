# TC : O(n) - Where it takes the length n of input list
# SC : O(1) - Only a few extra variables are used regardless of input size
class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        return nums[0]


# TC: O(log(n)) - The search space is halved each round until the minimum is found
# SC: O(1) - Only a few extra variables are used regardless of input size
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (high + low) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]
