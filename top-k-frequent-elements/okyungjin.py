from collections import Counter
import heapq
from typing import List

# [요구사항]
# - 정수 배열 nums과 정수 k가 주어진다.
# - 가장 자주 나타나는 k개의 숫자를 반환한다.
# - 결과는 아무 순서로 정렬해도 된다.

# [접근법]
# 1. for문을 순회하며 숫자의 빈도수를 계산한다
# 2. 빈도를 내림차순으로 정렬해서 상위 k개를 추출한다.

# [더 알아볼 것]
# - most_common(k)의 시간 복잡도가 왜 O(nlogK)일까?

# [알게된 것]
# - 역순 탐색은 `for n in reversed(nums)` 구문으로 간결하게
# - collections에 Counter를 사용하면 간결한 구문으로 빈도를 셀 수 있다
# - Counter는 most_common() 메서드를 제공한다.
# - dict는 `counter.get(n, 0)`를 사용해서 기본값을 편하게 설정할 수 있다.


# Solution A: collections Counter 사용해서 집계 후 most_common 메서드 사용
# - Time: O(nlogK) TODO
# - Space: O(N)
# - Runtime: 2ms  / Beats 91.48%
# - Memory: 22.83MB / Beats 60.93%
class SolutionA:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         # Counter가 counter 이터러블을 반환함
        counter = Counter(nums) # Space: O(N)

        # most_common 메서드로 빈도수 높은 k개 추출 -> (num, count) 튜플
        # Testcase1에서 counter.most_common(k)는 [(1, 3), (2, 2)]을 반환한다.
        # for 문으로 튜플을 까서 num만 사용한다
        return [num for num, _ in counter.most_common(k)] # Time: O(nlogK)

# Solution B: 빈도수 집계 -> 내림차순 정렬 -> k개 슬라이스
# - Time: O(nlogN)
# - Space: O(N)
# - Runtime: 3ms  / Beats 89.31%
# - Memory: 22.75MB / Beats 80.99%
class SolutionB:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter: dict[int, int] = {} # Space: O(N)

        # 숫자의 빈도수를 기록
        for n in nums:
            counter[n] = counter.get(n, 0) + 1 # dict 기본값 함수
        
         # 빈도수로 내림차순 정렬 후 k개 슬라이스
        return sorted(counter, key=counter.get, reverse=True)[:k] # Time: O(nlogN) by 정렬
     
# Solution C: 빈도별 숫자 목록을 저장하는 freqList 생성 (count sort)
# - Time: O(N)
# - Space: O(N)
# - Runtime: 8ms  / Beats 33.04%
# - Memory: 22.89MB / Beats 60.93%
class SolutionC:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 숫자별 카운트 집계
        counter: dict[int, int] = {} # Space: O(N)
        maxCnt = 1 
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
            maxCnt = max(counter[n], maxCnt) # 최대 빈도수를 기록한다 (freqList 최적화를 위함)

        # maxCount 길이인 [[], [], ..., []] 배열을 미리 생성해둔다
        # nums[idx]는 빈도수가 idx + 1인 숫자들이 들어간다.

        freqList = [[] for _ in range(maxCnt)]

        for num, cnt in counter.items():
            freqList[cnt - 1].append(num)

        # 예시)
        # nums=[1, 1, 1, 2, 2, 3], k=2 이라면 1은 3번, 2는 2번, 3은 1번 등장한다.
        # freqList는 [[3], [2], [1]] 가 된다.
            
        result = [] # Space: O(N)
        for bucket in reversed(freqList): # Time: O(N), 역순 탐색은 reversed로 간결하게
            if len(result) == k: # 해가 유니크하므로 등치로 비교
                return result # result도 slice 안 하고 그대로 반환
            result.extend(bucket)

        return result

# Solution D: 파이썬의 heapq 라이브러리 사용하여 최소힙으로 정렬
#  - Time: O(N logN)
# - Space: O(N)
# - Runtime: 7ms  / Beats 51.93%
# - Memory: 23.00MB / Beats 42.12%
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        counter = Counter(nums)

        # heapq 라이브러리는 최소힙으로 구현되어 있어서
        # 우선순위를 높아려면 count를 음수로 저장해야함
        heap = []
        for num, count in counter.items():
            heapq.heappush(heap, (-count, num))

        result = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            result.append(num)
        
        return result
    

print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))          # [1, 2]
# print(Solution().topKFrequent([1], 1))                         # [1]
# print(Solution().topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2)) # [1, 2]
# print(Solution().topKFrequent([4, 4, 4, 6, 6, 7], 1))           # [4]
# print(Solution().topKFrequent([1, 1, 2, 0, 0, 0], 2))           # [0, 1]
# print(Solution().topKFrequent([-1, -1, -1, 2, 2, 3], 2))        # [-1, 2]
