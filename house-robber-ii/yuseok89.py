# TC: O(N)
# SC: O(1)
class Solution:
    def rob(self, nums: list[int]) -> int:

        n = len(nums)

        def calc(nums, s, e):
            rob, skip = 0, 0
            for idx in range(s, e):
                rob, skip = skip + nums[idx], max(rob, skip)

            return max(rob, skip)

        if n == 1:
            return nums[0]

        return max(calc(nums, 0, n - 1), calc(nums, 1, n))

