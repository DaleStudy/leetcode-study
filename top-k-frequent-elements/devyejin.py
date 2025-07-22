from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        counter = sorted(Counter(nums).items(), key=lambda item: -item[1])
        return list(num for num, count in counter[:k])

