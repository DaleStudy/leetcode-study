from typing import List


class Solution:
    # Time: O(n)
    # Space: O(n)
    def maxProduct(self, nums: List[int]) -> int:
        maxProducts = [nums[0]]
        minProducts = [nums[0]]
        # Store all max/minProducts[i]: the max/min product of all subarrays that have nums[i] as the last element.
        # Time: O(n)
        # Space: O(n)
        for num in nums[1:]:
            newMaxProduct = max(maxProducts[-1] * num, minProducts[-1] * num, num)
            newMinProduct = min(maxProducts[-1] * num, minProducts[-1] * num, num)
            maxProducts.append(newMaxProduct)
            minProducts.append(newMinProduct)
        return max(maxProducts)
