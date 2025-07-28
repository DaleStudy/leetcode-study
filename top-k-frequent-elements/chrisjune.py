from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        l = [(k, v) for k, v in dic.items()]
        l.sort(reverse=True, key=lambda x: x[1])
        l = [i for i, _ in l]
        return l[:k]
