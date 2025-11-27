"""
time complexity: O(nlogn)
space complexity: O(n)
"""

from typing import List
from collections import Counter
from heapq import nlargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [num for num, _ in nlargest(k, count.items(), key=lambda x: x[1])]



