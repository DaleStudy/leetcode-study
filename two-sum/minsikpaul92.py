class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range (len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]