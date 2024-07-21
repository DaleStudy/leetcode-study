class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1

        for i in range(target, -1, -1):
            if i + nums[i] >= target:
                target = i

        return True if target == 0 else False

        # maxReach = 0
        # for i, jump in enumerate(nums):
        #     if i > maxReach:
        #         return False
        #     maxReach = max(maxReach, i + jump)
        # return True

        ## Both TC: O(n), SC: O(1)
