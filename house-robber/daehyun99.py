# Time: O(N)
# Space: O(N)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        len_nums = len(nums)
        cum_sum = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            if i - 3 >= 0:
                val1 = cum_sum[i-2] + nums[i]
                val2 = cum_sum[i-3] + nums[i]
                cum_sum[i] = max(val1, val2)
            elif i - 2 >= 0:
                cum_sum[i] = cum_sum[i-2] + nums[i]
            else:
                cum_sum[i] = nums[i]
        return max(cum_sum)
