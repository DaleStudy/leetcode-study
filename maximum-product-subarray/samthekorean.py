# TC : O(n)
# SC : O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_overall = nums[0]
        current_min_product = current_max_product = 1

        for num in nums:
            temp_min = min(current_min_product * num, current_max_product * num, num)
            current_max_product = max(
                current_min_product * num, current_max_product * num, num
            )
            current_min_product = temp_min
            max_overall = max(current_max_product, max_overall)

        return max_overall
