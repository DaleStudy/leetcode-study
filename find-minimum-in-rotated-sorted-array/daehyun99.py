class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        while True:
            if nums[-1] < nums[0]:
                nums[0] = nums.pop()
            else:
                break

        return nums[0]

"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
"""
