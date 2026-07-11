import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        count = dict()
        heap = []
        if len(nums) <= 1:
            return nums
        # O(N)
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # heap 의 크기는 최대 k 로 제한함.
        # unique 한 M개의 숫자를 선형 순회 O(M)
        for num, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))         # O(logK)
            else:
                if heap[0][0] < freq:
                    heapq.heappop(heap)         # O(logK)
                    heapq.heappush(heap, (freq, num))         # O(logK)

        for _ in range(k):
            k, v = heapq.heappop(heap)
            answer.append(v)

        return answer

