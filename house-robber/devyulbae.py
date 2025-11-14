"""
blind75 - House Robber
LeetCode Problem: https://leetcode.com/problems/house-robber/

재귀
F(x) = F(x+1), F(x+2) + nums[x] 중 큰 값을 계속 선택하면 된다
-> 재귀를 2번씩 호출하기 때문에 시간복잡도는 O(2^n)으로 Time Limit Exceeded 발생
다음 주차 때 다시 풀어보자.
dp로도 될 거 같다
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        def dfs(s):
            if s >= len(nums):
                return 0
            return max(dfs(s+1), nums[s] + dfs(s+2))
        
        return dfs(0)
        
        