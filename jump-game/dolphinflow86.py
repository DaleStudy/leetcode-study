# N is the length of array nums.
# TC: O(N) - single pass maintaining maximum reachable index
# SC: O(1) - uses constant extra space


class Solution:

    def canJump(self, nums) -> bool:
        max_reach = 0

        for i, num in enumerate(nums):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + num)

            if max_reach >= len(nums) - 1:
                return True

        return True
