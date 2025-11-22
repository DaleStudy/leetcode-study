from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [idx, seen[need]]
            seen[num] = idx

