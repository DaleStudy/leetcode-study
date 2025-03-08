# Time Complexity:
#   - addNum(): O(log N) - use a heap operation (push/pop) which takes log N time.
#   - findMedian(): O(1) - just accessing the top elements of heaps.
# Space Complexity: O(N) - store all elements in two heaps.


class MedianFinder:
    def __init__(self):
        # max heap (stores the smaller half of numbers, negated values for max heap behavior)
        self.maxHeap = []
        # min heap (stores the larger half of numbers)
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= -self.maxHeap[0]:
            # store as negative to simulate max heap
            heapq.heappush(self.maxHeap, -num)  
        else:
            heapq.heappush(self.minHeap, num)

        # balance the heaps: maxHeap can have at most 1 more element than minHeap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]  # odd number of elements, maxHeap has the median
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0  # even case, average of two middle numbers
