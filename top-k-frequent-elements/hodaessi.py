from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1

        return sorted(dict.keys(), key=lambda x: dict[x], reverse=True)[:k]
