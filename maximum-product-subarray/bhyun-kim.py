"""
152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Solution: Dynamic Programming
    To solve this problem, we need to keep track of the maximum product and minimum product so far.
    The minimum product can become the maximum product when multiplied by a negative number.

    - Initialize min_so_far and max_so_far to the first element of the input array.
    - Iterate through the input array starting from the second element.
        - Update min_so_far and max_so_far with the current element.
        - Update max_product with the maximum of max_so_far and max_product.
    - Return max_product.

Time complexity: O(n)
    - We iterate through the input array once.

Space complexity: O(1)
    - We use only a constant amount of space.


"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_so_far = nums[0]
        max_so_far = nums[0]
        max_product = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            min_so_far, max_so_far = min(
                curr, max_so_far * curr, min_so_far * curr
            ), max(curr, max_so_far * curr, min_so_far * curr)
            max_product = max(max_so_far, max_product)

        return max_product
