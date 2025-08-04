"""
Constraints:
- -10^5 <= num <= 10^5
- There will be at least one element in the data structure before calling findMedian.
- At most 5 * 10^4 calls will be made to addNum and findMedian.

<Solution 1: 리스트 활용>

Time Complexity: 
- addNum(): O(nlogn)
  - 매번 정렬하기 때문
- findMedian(): O(1)
  - 정렬된 리스트에서 인덱스 접근

Space Complexity: O(n)
- 입력된 모든 숫자를 리스트에 저장

풀이방법:
1. 리스트 자료구조 사용
2. 리스트에 각 요소들 추가 후 정렬
3. 리스트의 요소 갯수가 홀수/짝수일 때의 경우를 나눠서 median 값을 구함

메모: 
- heap이 익숙하지 않아서 일단 리스트로 문제를 풀었습니다.
- 나중에 heap으로 다시 풀기
"""
class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()
        

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 1:
            return self.nums[n // 2]
        else:
            mid1 = self.nums[n // 2 - 1]
            mid2 = self.nums[n // 2]
            return (mid1 + mid2) / 2.0

"""
<Solution 2: 힙 활용>

Time Complexity:
- addNum(): O(log n) - 힙에 삽입/삭제 연산
- findMedian(): O(1) - 힙의 루트 요소만 접근

Space Complexity: 
- O(n) - 모든 입력 숫자를 두 개의 힙에 저장

풀이방법:
max/min heap을 사용해서 데이터를 절반씩 나누어 median 값을 찾음
1. 자료구조
  - lower (max heap)
  - upper (min heap)
2. addNum
  - upper가 비어있거나 새로운 숫자가 upper[0]보다 크면 upper에 추가
  - 그렇지 않으면 lower에 추가
3. 균형 유지
  - 두 힙의 크기 차이가 최대 1이 되도록 조정함
  - lower가 더 많으면 upper로 이동
  - upper가 2개 이상 더 많으면 lower로 이동
4. 중간값 계산
  - 홀수개: upper[0] (upper가 항상 1개 더 많거나 같기 때문)
  - 짝수개: (-lower[0] + upper[0]) / 2
"""
from heapq import heappop, heappush

class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if not self.upper or self.upper[0] < num:
            heappush(self.upper, num)
        else:
            heappush(self.lower, -num)

        if len(self.lower) > len(self.upper):
            heappush(self.upper, -heappop(self.lower))
        elif len(self.lower) + 1 < len(self.upper):
            heappush(self.lower, -heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) < len(self.upper):
            return self.upper[0]

        else:
            return (-self.lower[0] + self.upper[0]) / 2
