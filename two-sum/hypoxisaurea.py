from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]

            for j in range(i+1, len(nums)):
                if nums[j] == diff:
                    return [i, j]

        raise ValueError('No answer')


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in lookup:
                return [lookup[diff], i]
                
            lookup[num] = i

        raise ValueError('No answer')