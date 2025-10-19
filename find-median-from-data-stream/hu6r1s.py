class MedianFinder:

    def __init__(self):
        self.median_finder = []

    def addNum(self, num: int) -> None:
        self.median_finder.append(num)

    def findMedian(self) -> float:
        self.median_finder.sort()
        mid = len(self.median_finder) // 2
        if len(self.median_finder) % 2:
            return self.median_finder[mid]
        else:
            return (self.median_finder[mid-1] + self.median_finder[mid]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
