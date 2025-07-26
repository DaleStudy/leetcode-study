'''
Bucket Sort 접근:
    1. Counter로 각 숫자의 빈도를 계산한다.
    2. 빈도 수를 인덱스로 하는 버킷(buckets)을 생성한다.
        - buckets[i]에는 등장 횟수가 i번인 숫자들이 들어간다.
    3. 버킷의 가장 높은 빈도 인덱스부터 역순으로 순회하며
        숫자를 하나씩 결과 리스트(result)에 추가한다.
    4. 결과 리스트에 k개가 모이면 반환한다.

시간 복잡도: O(n)
    - 빈도 계산 O(n)
    - 버킷 채우기 O(n)
    - 결과 수집 O(n)

공간 복잡도: O(n)
    - Counter 딕셔너리와 버킷 리스트 사용
'''


from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
            
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                
                if len(result) == k:
                    return result
                
        return result