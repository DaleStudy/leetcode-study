# N is the length of array nums.
# TC: O(N) - single pass maintaining maximum and minimum product
# SC: O(1) - uses constant extra variables


class Solution:

    def maxProduct(self, nums) -> int:
        if not nums:
            return 0

        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                cur_max, cur_min = cur_min, cur_max

            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)

            res = max(res, cur_max)

        return res
