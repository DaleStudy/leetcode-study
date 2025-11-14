"""
Blind75 - 5. Maximum Subarray
LeetCode Problem Link: https://leetcode.com/problems/maximum-subarray/

통과는 했는데 시간복잡도 O(n^2)라서 좀 아쉽다...투포인터로 풀 수도 있을 거 같은데...
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = nums[0]

        for s in range(len(nums)):
            total = 0
            for e in range(s, len(nums)):
                total += nums[e]
                if total > max_total:
                    max_total = total
        return max_total