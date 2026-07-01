# - 문제: https://leetcode.com/problems/top-k-frequent-elements/
# - 풀이: https://www.algodale.com/problems/top-k-frequent-elements/

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [num for num, count in counter.most_common(k)]

