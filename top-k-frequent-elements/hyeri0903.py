import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for n in nums:
            if n in table:
                table[n] += 1
            else:
                table[n] = 1
        #sol 1) sorting 사용한 case
        # sorted_table = sorted(table.items(), key=lambda x:x[1], reverse = True)
        # return [ key for key, freq in sorted_table[:k]]

        #sol 2) min heap 사용한 case
        #convert the frequencies to negative values so it return first
        heap = [(-freq, key) for key, freq in table.items()]
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            freq, key = heapq.heappop(heap)
            res.append(key)
        return res
