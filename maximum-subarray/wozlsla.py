"""
# Intuition
- X
# Approach
- X
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_total = nums[0]

        for i in range(len(nums)):  # O(N)
            for j in range(i, len(nums)):  # O(N)

                max_total = max(sum(nums[i : j + 1]), max_total)  # O(N)

        return max_total
