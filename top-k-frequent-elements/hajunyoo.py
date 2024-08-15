from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = defaultdict(int)

        for n in nums:
            counter_dict[n] += 1

        count_list = []
        for key, val in counter_dict.items():
            count_list.append((key, val))

        count_list.sort(key=lambda x: x[1], reverse=True)
        answer = [a for a, b in count_list[:k]]

        return answer