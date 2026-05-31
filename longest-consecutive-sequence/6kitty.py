#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
from typing import List
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        long=0

        leng=1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            if nums[i]+1==nums[i+1]:
                leng+=1
            else:
                long=max(long,leng)
                leng=1
        # 아래를 추가해야 for문 다 돌았을 때 leng이 최고인 경우 반영
        long=max(long,leng)
        return long
        
        
# @lc code=end

