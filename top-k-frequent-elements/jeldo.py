from collections import Counter
import heapq


class Solution:
    # O(nlogn)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ls = [(key, value) for key, value in Counter(nums).items()]  # O(n)
        return [key for _, key in heapq.nlargest(n=k, iterable=ls)]  # O(nlogn)
