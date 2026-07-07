# TC: O(N)
# SC: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0] if nums[0] < 0 else 0
        ans = sum

        for num in nums:
            if num > sum + num:
                sum = num
            else:
                sum += num

            ans = max(ans, sum)

        return ans

