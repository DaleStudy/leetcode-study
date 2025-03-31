from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 빈도 계산
        count = Counter(nums)
        n = len(nums)
        
        # 빈도수를 기준으로 버킷 생성 (0에서 n까지)
        buckets = [[] for _ in range(n + 1)]
        
        # 각 숫자를 해당 빈도수의 버킷에 추가
        for num, freq in count.items():
            buckets[freq].append(num)
        
        # 빈도가 높은 순서대로 k개의 숫자를 추출
        result = []
        for freq in range(n, 0, -1):
            if buckets[freq]:
                result.extend(buckets[freq])
                
                if len(result) == k:
                    return result
