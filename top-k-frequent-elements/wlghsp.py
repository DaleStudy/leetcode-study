"""
 * Time Complexity: O(n + ulogk)
 * Space Complexity: O(n)
"""
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums_freq = {}
        for n in nums: # n번
            if n in nums_freq:
                nums_freq[n] += 1
            else:
                nums_freq[n] = 1
        heap = []
        for num, freq in nums_freq.items(): # u번 (unique한 원소 갯수)
            if len(heap) >= k:
                if heap[0][0] < freq:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq, num))
            else:
                heapq.heappush(heap, (freq, num))
        return [k for _, k in heap]
           