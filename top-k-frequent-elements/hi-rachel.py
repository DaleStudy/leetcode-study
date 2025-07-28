"""
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

TC: O(n log n)
SC: O(n)
"""

from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = defaultdict(int)

        for num in nums:
            numdict[num] += 1

        sort_dict = dict(sorted(numdict.items(), key=lambda item: item[1], reverse=True))

        keys = list(sort_dict)

        return keys[:k]
    
# heapq 풀이
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return heapq.nlargest(k, counter.keys(), key=counter.get)


