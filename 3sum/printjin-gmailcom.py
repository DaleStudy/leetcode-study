from typing import List
from itertools import combinations
class Solution:
    def threeSum(self, nums):
        res = set()
        n = len(nums)
        for i in range(n):
            a = nums[i]
            rest = nums[:i] + nums[i+1:] 
            for comb in combinations(rest, 2):
                if sum(comb) == -a:
                    triplet = tuple(sorted([a, *comb]))
                    res.add(triplet)
        return [list(t) for t in res]
