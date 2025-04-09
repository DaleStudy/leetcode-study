# Solution 1: using Counter, heapq
from collections import Counter
import heapq 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        return heapq.nlargest(k, count_dict.keys(), key=count_dict.get)

# Solution 2: create dict, use sorted function 
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq_dict = {}
#         for num in nums: 
#             if num in freq_dict: 
#                 freq_dict[num] += 1
#             else: 
#                 freq_dict[num] = 1
#         sorted_list = sorted(freq_dict.keys(), key = lambda x: freq_dict[x], reverse=True)
#         return sorted_list[:k]
        