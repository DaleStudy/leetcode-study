# Time: O(nk)
# Space: O(n)
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)

        for num in nums:
            nums_dict[num] += 1

        result = []
        for i in range(k):
            max_count = 0
            max_num = 0
            for num, count in nums_dict.items():
                if max_count < count:
                    max_count = count
                    max_num = num
            nums_dict[max_num] = 0
            result.append(max_num)
        return result
