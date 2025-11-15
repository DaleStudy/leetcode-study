from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for n in nums:
          if n not in nums_dict.keys():
            nums_dict[n] = 1
          else:
            nums_dict[n] += 1

        frequent_rank = sorted(nums_dict.items(), key=lambda item:item[1], reverse=True)
        return [frequent_rank[j][0] for j in range(k)]