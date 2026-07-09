# TC: O(N)
# SC: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0] if nums[0] < 0 else 0
        ans = sum

        for num in nums:
            sum = max(num, sum + num)
            ans = max(ans, sum)

        return ans

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         sum = nums[0]
#         ans = sum

#         for idx in range(1, len(nums)):
#             sum = max(nums[idx], sum + nums[idx])
#             ans = max(ans, sum)

#         return ans

