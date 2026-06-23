class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        import heapq

        heap = []
        cnt = {}

        for num in nums:
            if num not in cnt:
                cnt[num] = 0

            cnt[num] = cnt[num] + 1

        for num in cnt.keys():
            if len(heap) < k:
                heapq.heappush(heap, cnt[num])
            elif heap[0] < cnt[num]:
                heapq.heappop(heap)
                heapq.heappush(heap, cnt[num])

        ret = []

        for num in cnt.keys():
            if cnt[num] >= heap[0]:
                ret.append(num)

        return ret

