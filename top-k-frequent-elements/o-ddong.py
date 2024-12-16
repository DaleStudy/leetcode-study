import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, cnt in collections.Counter(nums).most_common(k)]
