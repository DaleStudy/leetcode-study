# TC (NlogN)
# SC (N)
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0 and len(self.max_heap) == 0:
            heapq.heappush(self.min_heap, num)
        elif len(self.max_heap) == 0:
            mid = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min(mid, num))
            heapq.heappush(self.min_heap, max(mid, num))
        elif len(self.max_heap) == len(self.min_heap):
            mid1 = -self.max_heap[0]
            mid2 = self.min_heap[0]

            if num <= mid1:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
        else:
            if len(self.max_heap) > len(self.min_heap):
                mid = -heapq.heappop(self.max_heap)
            else:
                mid = heapq.heappop(self.min_heap)

            heapq.heappush(self.max_heap, -min(mid, num))
            heapq.heappush(self.min_heap, max(mid, num))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            mid1 = -self.max_heap[0]
            mid2 = self.min_heap[0]
            return (mid1 + mid2) / 2.0
        else:
            if len(self.max_heap) > len(self.min_heap):
                return float(-self.max_heap[0])
            else:
                return float(self.min_heap[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

