# 시간복잡도: O(Nlog N)
# 공간복잡도: O(N)
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, count in Counter(nums).most_common(k)]
