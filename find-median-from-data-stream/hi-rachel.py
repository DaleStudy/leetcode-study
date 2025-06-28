# 두 개로 나눠서 저장하면,
# 홀수개의 숫자일 경우: 첫 번째에서 가장 큰 값이나 두 번째에서 가장 작은 값이 중앙값
# 짝수개의 숫자일 경우: 첫 번째에서 가장 큰 값과 두 번째에서 가장 작은 값의 평균
# => 힙 활용
# 숫자 추가시 작은 값들 => 최대 힙, 큰 값들 => 최소 힙에 음수로 저장! 최대 힙의 모든 값 ≤ 최소 힙의 모든 값
# 최대 힙에서 가장 큰 값을 최소 힙으로 이동
# 만약 최소 힙 크기가 더 크면 다시 하나를 최대 힙으로 이동
# 두 힙간의 크기 차이 항상 0 또는 1 유지
# TC: addNum O(log n), findMedian O(1)
# SC: O(n)

import heapq

class MedianFinder:
    def __init__(self):        
        self.max_heap = []  # 최대 힙 (음수로 저장) 
        self.min_heap = []  # 최소 힙

    def addNum(self, num: int) -> None:
        # 1. 최대 힙에 먼저 삽입 (음수로)
        heapq.heappush(self.max_heap, -num)

        # 2. max_heap에서 가장 큰 값을 min_heap으로 옮김 (오름차순 정렬 유지)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
    
        # 3. min_heap이 max_heap보다 커지면, 다시 max_heap으로 옮김 (균형 유지)
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
