# https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, nums):
        
        prev = 0
        prev_2 = 0

        for num in nums:
            cur = max(prev, prev_2 + num)

            prev_2 = prev
            prev = cur

        return prev
