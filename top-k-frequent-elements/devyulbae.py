"""
Blind75 - top-k-frequent-elements
https://leetcode.com/problems/top-k-frequent-elements/
"""

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # (1,1,2,2,2,3) -> {1:1, 2:3, 3:1}
        num_counter = Counter(nums) 
        # {1:1, 2:3, 3:1} -> [(2,3), (1,1), (3,1)]
        sorted_items = sorted(num_counter.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]