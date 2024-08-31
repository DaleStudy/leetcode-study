from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i, n in enumerate(nums):
            complement = target - n

            if complement in index_map:
                return [index_map[complement], i]
            index_map[n] = i
