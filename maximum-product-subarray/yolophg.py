# Time Complexity: O(N) - just one pass through the array, so it's linear time.
# Space Complexity: O(1) - no extra arrays, just a few variables.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # tracking max product from both ends
        prefix_product, suffix_product = 1, 1  
        # start with the biggest single number
        max_product = max(nums)  

        for i in range(len(nums)):
            # move forward, multiplying
            prefix_product *= nums[i]  
            # move backward, multiplying
            suffix_product *= nums[len(nums) - i - 1]  
            # update max product
            max_product = max(max_product, prefix_product, suffix_product)

            # if hit zero, reset to 1 (zero kills the product chain)
            if prefix_product == 0:
                prefix_product = 1
            if suffix_product == 0:
                suffix_product = 1

        return max_product
