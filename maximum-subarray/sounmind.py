from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find the contiguous subarray with the largest sum using Kadane's algorithm.

        Args:
            nums: List of integers

        Returns:
            Maximum subarray sum
        """
        if not nums:
            return 0

        global_max = local_max = nums[0]

        for num in nums[1:]:
            # Either start a new subarray with current element or extend previous subarray
            local_max = max(num, local_max + num)
            # Update global maximum if current local maximum is greater
            global_max = max(global_max, local_max)

        return global_max
