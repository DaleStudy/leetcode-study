#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre=0
        cur=0
        for num in nums:
            pre, cur = cur, max(num + pre, cur)
        return cur
        
# @lc code=end

