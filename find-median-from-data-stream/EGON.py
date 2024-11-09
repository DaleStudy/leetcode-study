from heapq import heappush, heappop
from unittest import TestCase, main


class MedianFinder:
    """
    Runtime: 137 ms (Beats 56.16%)
    Time Complexity:
        1) addNum
            - 최악의 경우 heappush + (heappop + heappush) + (heappop + heapppush) 가 발생할 수 있으므로 O(5 * log n)
            > O(5 * log n) ~= O(log n)
        2) findMedian
            > heap의 루트 값을 가지고 사칙연산만 하므로 O(1)

    Memory: 39.94 MB (Beats 5.85%)
    Space Complexity: O(n)
        - max_heap은 최대 n // 2 개 혹은 n // 2 + 1개의 원소를 가지므로 O(n / 2 + 1), upper bound
        - min_heap은 최대 n // 2개의 원소를 가지므로 O(n / 2)
        > O(n / 2 + 1) + O(n / 2) ~= O(n) + O(n) ~= O(n)
    """

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        heappush(self.max_heap, -num)
        if self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            heappush(self.min_heap, -heappop(self.max_heap))

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self):
        if self.max_heap and self.min_heap:
            if len(self.max_heap) == len(self.min_heap):
                return ((-self.max_heap[0]) + self.min_heap[0]) / 2
            else:
                return -self.max_heap[0]
        elif self.min_heap and not self.max_heap:
            return self.min_heap[0]
        elif not self.min_heap and self.max_heap:
            return -self.max_heap[0]
        else:
            return 0.0


class _LeetCodeTestCases(TestCase):

    def test_1(self):
        medianFinder = MedianFinder()
        medianFinder.addNum(-1)
        self.assertEqual(medianFinder.findMedian(), -1.0)
        medianFinder.addNum(-2)
        self.assertEqual(medianFinder.findMedian(), -1.5)
        medianFinder.addNum(-3)
        self.assertEqual(medianFinder.findMedian(), -2.0)
        medianFinder.addNum(-4)
        self.assertEqual(medianFinder.findMedian(), -2.5)
        medianFinder.addNum(-5)
        self.assertEqual(medianFinder.findMedian(), -3.0)


if __name__ == '__main__':
    main()
