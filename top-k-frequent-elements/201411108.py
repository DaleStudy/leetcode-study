# n : nums의 길이, m : 고유한 숫자의 개수
# TC(n), 버킷 정렬에서 n + m 개를 조회하기 때문에 O(n + m) = O(n)이다. (m <= n)
# SC(n)
# - dictionary O(m)
# - buckets O(n + 1 + m), 버킷의 수는 n + 1개, 내부에 저장된 숫자는 m개
# - result O(k)
# - O(m + n + k)에서 k <= m <= n이므로 O(n)
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dictionary = defaultdict(int)

        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in dictionary.items():
            buckets[freq].append(num)
        
        result = []

        # 인덱스가 등장 빈도를 의미하기 때문에 역순으로 조회
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

