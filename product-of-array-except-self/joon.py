from typing import List
from functools import reduce


class Solution:
    # Time: O(n)
    # Space: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size: int = len(nums)
        if size == 1:
            return [1]
        # 1. Cut the array at the middle.
        # Time: O(1)
        # Space: O(n)
        indexToCut: int = len(nums) // 2
        left: List[int] = nums[0:indexToCut]
        right: List[int] = nums[indexToCut:size]

        # 2. Divide, conquer, and merge. But no benefit in complexity.
        # Time: O(n)
        # Space: O(n)
        return self.multiplyToAll(self.productExceptSelf(left), self.calculateProductAll(right)) + self.multiplyToAll(self.productExceptSelf(right), self.calculateProductAll(left))

    def calculateProductAll(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x * y, nums)

    def multiplyToAll(self, nums: List[int], multiplier: int) -> List[int]:
        return list(map(lambda num: multiplier * num, nums))
