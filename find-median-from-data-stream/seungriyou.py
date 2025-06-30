# https://leetcode.com/problems/find-median-from-data-stream/

import heapq

class MedianFinder:
    """
    [Time Complexity]
        - addNum(): O(logn) (heappush / heappop -> 힙 속성 유지 위해 트리 높이만큼 swap => sift-up / sift-down)
        - findMedian(): O(1)

    [Approach]
        findMedian을 O(1)에 수행하기 위해서는 addNum을 할 때마다 데이터를 작은 부분 / 큰 부분으로 절반씩 나누어서 유지해야 한다.
        이때, 가능한 케이스별 median을 구하는 방법은 다음과 같다.
            - 두 절반의 길이가 같다면 median = ((작은 부분의 가장 큰 값) + (큰 부분의 가장 작은 값)) / 2
            - 두 절반의 길이가 다르다면 (큰 부분의 길이가 작은 부분의 길이보다 1 큰 경우라고 가정) median = (큰 부분의 가장 작은 값)
        따라서 작은 부분 / 큰 부분을 각각 max heap / min heap으로 관리하며, addNum 할 때마다 다음은 동작을 수행한다.
            - 두 절반의 길이가 같다면, 작은 부분에 push -> pop 한 결과를 큰 부분에 push
            - 두 절반의 길이가 다르다면, 큰 부분에 push -> pop 한 결과를 작은 부분에 push
        (파이썬에서 max heap을 사용하기 위해서는 min heap에 부호 반전인 수를 넣음으로써 구현하는 것에 유의한다!)
    """

    def __init__(self):
        self.lo = []  # 절반 중 작은 부분
        self.hi = []  # 절반 중 큰 부분

    def addNum(self, num: int) -> None:
        if len(self.lo) == len(self.hi):
            heapq.heappush(self.hi, -heapq.heappushpop(self.lo, -num))  # heappushpop: heap을 한 번만
        else:
            heapq.heappush(self.lo, -heapq.heappushpop(self.hi, num))

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (-self.lo[0] + self.hi[0]) / 2
        else:
            return self.hi[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
