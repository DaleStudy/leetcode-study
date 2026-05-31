#idea : DP
# Time Complexity: O(n)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 0
        max_prod = min_prod = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(nums[i], max_prod * nums[i])
            min_prod = min(nums[i], min_prod * nums[i])

            ans = max(ans, max_prod)

        return ans


# Time Complxity: O(N^2)
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         max_product = nums[0]
#         for s in range(len(nums)):
#             product = 1
#             for e in range(s, len(nums)):
#                 product *= nums[e]
#                 max_product = max(product, max_product)
#         return max_product


