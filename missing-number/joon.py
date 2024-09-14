from typing import List


class Solution:
    # Time: O(n)
    # Space: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # MissingNumber = (Sum of 1, 2, ..., n) - Sum of nums)
        # Time: O(n)
        return n * (n + 1) // 2 - sum(nums)
