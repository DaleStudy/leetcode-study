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

Space Complexity: 

풀이방법:

"""
from heapq import heappop, heappush

