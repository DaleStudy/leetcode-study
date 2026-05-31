#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # list로 하니까 시간 초과 떠서 set으로 변경
        idx=set()
        for i in nums:
            if i in idx:
                return True
            idx.add(i)
        # null 방지 
        return False
        
# @lc code=end

