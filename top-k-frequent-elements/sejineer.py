"""
시간 복잡도 O(N)
공간 복잡도 O(N)

Priority Queue 를 이용한 풀이
시간 복잡도 O(Nlog(N))
공간 복잡도 O(N)
from queue import PriorityQueue
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        que = PriorityQueue()

        for num, freq in counter.items():
            que.put((-freq, num))
        
        res = []

        for _ in range(k):
            res.append(que.get()[1])

        return res
"""
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            bucket[freq].append(num)

        result = []

        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                for num in bucket[i]:
                    result.append(num)
                    if len(result) == k:
                        return result
