from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            second_value = target - v
            
            if second_value in nums[i+1:]:
                return [i, nums[i+1:].index(second_value) + i+1]