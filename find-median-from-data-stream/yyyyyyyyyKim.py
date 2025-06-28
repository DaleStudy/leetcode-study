class MedianFinder:
    # Follow up : 두 개의 heap 사용해서 구현 가능(시간복잡도 O(log n), 추가 공부 필요함)
    # heap 사용하지 않고 이진 탐색 삽입으로 풀었음

    def __init__(self):
        # 숫자 저장할 리스트 생성
        self.arr = []
        

    def addNum(self, num: int) -> None:
        # 숫자 추가하고 정렬하기
        # self.arr.append(num)
        # self.arr.sort()   -> 시간초과(시간복잡도 O(n log n))
        # 이진탐색삽입(시간복잡도 O(n))
        bisect.insort(self.arr, num)

    def findMedian(self) -> float:
        # 길이가 홀수면 가운데 값 리턴
        if len(self.arr)%2 == 1:
            return self.arr[len(self.arr)//2]
        # 길이가 짝수면 가운데 두 수의 평균 리턴
        return (self.arr[len(self.arr)//2-1] + self.arr[len(self.arr)//2]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
