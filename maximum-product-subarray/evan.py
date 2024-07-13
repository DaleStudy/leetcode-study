from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        local_max_product = nums[0]
        min_product = nums[0]
        global_max_product = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]

            temp_max = max(
                # the current element alone could be the new maximum product subarray.
                current,

                # extending the previous maximum product subarray to include the current element.
                local_max_product * current,

                # if the current element is negative, multiplying it by the previous minimum product subarray
                # (which could be a large negative number) might result in a large positive number,
                # thus becoming the new maximum product.
                min_product * current,
            )
            min_product = min(
                current, local_max_product * current, min_product * current
            )
            local_max_product = temp_max

            global_max_product = max(global_max_product, local_max_product)

        return global_max_product
