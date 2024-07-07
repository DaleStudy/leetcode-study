class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, not_rob = 0, 0

        for i in nums:
            rob, not_rob = not_rob + i, max(rob, not_rob)

        return max(rob, not_rob)

        ## TC: O(n), SC: O(1)
