"""
https://leetcode.com/problems/top-k-frequent-elements/description/

시간 복잡도: O(n log n)
- 모든 숫자의 빈도 계산 O(n)
- 빈도가 높은 k개 선택 O(n log k)
- 결과 리스트 생성 O(k)

공간 복잡도: O(n)
- 고유 숫자별 빈도 저장 O(n)
- 정답 k개 저장 O(k)
"""

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        answer = [n for n, f in counts.most_common(k)]
        
        return answer
