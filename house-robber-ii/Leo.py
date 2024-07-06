class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def robrob(nums):
            rob1, rob2 = 0, 0
            for i in range(len(nums)):
                rob1, rob2 = rob2, max(nums[i] + rob1, rob2)

            return rob2

        return max(robrob(nums[:n - 1]), robrob(nums[1:]))

        ## TC: O(n), SC: O(1)
