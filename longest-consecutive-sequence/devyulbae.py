"""
Blind75 - Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/

조건 : O(n) 시간복잡도
1. 시작점이면 초기화
2. 아니면 cnt++
3. 끊기면 max 갱신
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        length = 1
        max_length = 0
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            elif nums[i+1] == nums[i] + 1:
                length += 1
            else:
                max_length = max(max_length, length)
                length = 1
        
        max_length = max(max_length, length)
        return max_length

