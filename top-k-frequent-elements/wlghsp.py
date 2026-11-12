"""
 * Time Complexity: O(n)
 * Space Complexity: O(n)
"""
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 1. 빈도 계산: O(N)
        count = Counter(nums)

        # 2. 빈도를 인덱스로 사용하는 버킷 배열 생성: O(N)
        # 최대 빈도는 len(nums)이므로 크기는 len(nums) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        # 3. 높은 빈도(뒤쪽 인덱스)부터 k개 추출: O(N)
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
