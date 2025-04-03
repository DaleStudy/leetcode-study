# 가장 자주 등장한 상위 K개의 문자 배열 반환
# O(n log n) time, O(n) space

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = defaultdict(int);
        result = []

        for num in nums:
            if num in numdict:
                numdict[num] += 1
            else:
                numdict[num] = 1

        sort_dict = dict(sorted(numdict.items(), key=lambda item: item[1], reverse=True))

        keys = list(sort_dict)

        return keys[:k]
