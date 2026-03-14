# Goal: Return an array answer that product of all elements except nums[i].
#
# Approach:
# Use prefix&suffix arrays to store cumulative products
# - prefix: product of elements to the left of i
# - suffix: product of elements to the right of i
# Calculate the result[i] by multipying prefix[i] and suffix[i]
#
# Time Complexity: O(n)
# - We Iterate the array to compute prefix, suffix and result.
# Space Complexity: O(n)
# - We use extra arrays for prefix&suffix.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]
        
        return result
