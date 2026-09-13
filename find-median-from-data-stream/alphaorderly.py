"""
시간 복잡도: O(LogN)
공간 복잡도: O(N)

최소 힙에는 스트림의 중간값보다 크거나 같은 값들이 저장됨
최대 힙에는 스트림의 중간값보다 작은 값들이 저장됨

두 힙의 경계에 위치한 값을 이용해 중간값을 구한다
"""
class MedianFinder:

    def __init__(self):
        self.min = []
        self.max = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.max, num)
        heapq.heappush(self.min, heapq.heappop_max(self.max))

        if len(self.min) > len(self.max):
            heapq.heappush_max(self.max, heapq.heappop(self.min))

    def findMedian(self) -> float:
        if len(self.max) == len(self.min):
            return (self.min[0] + self.max[0]) / 2
        else:
            return self.max[0]