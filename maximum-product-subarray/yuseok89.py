# TC: O(N)
# SC: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ans = nums[0]
        max_val, min_val = 1, 1

        for num in nums:
            temp = max_val * num
            max_val = max(temp, min_val * num, num)
            min_val = min(temp, min_val * num, num)

            ans = max(ans, max_val)

        return ans

