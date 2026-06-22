from typing import List

"""
Ideation
    해시맵에 각 원소별 빈도수를 저장한 뒤, 빈도수 높은 순으로 정렬한 다음 앞에서 k개를 반환합니다.
Time Complexity: O(n)
Space Complexity: O(n + m log m)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        sorted_nums = sorted(frequency, key=lambda num: frequency[num], reverse=True)

        return sorted_nums[:k]


