"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray

Solution:
    To solve this problem, we can use the Kadane's algorithm.
    We keep track of the current sum and the maximum sum.
    We iterate through the array and update the current sum and maximum sum.
    If the current sum is greater than the maximum sum, we update the maximum sum.
    We return the maximum sum at the end.

Time complexity: O(n)
    - We iterate through each element in the array once.

Space complexity: O(1)
    - We use a constant amount of extra space.
"""


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
