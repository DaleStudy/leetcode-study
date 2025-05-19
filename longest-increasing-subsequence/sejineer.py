"""
시간 복잡도: O(Nlog(N))
공간 복잡도: O(N)
"""
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            index = bisect_left(sub, num)
            if index == len(sub):
                sub.append(num)
            else:
                sub[index] = num
        return len(sub)
