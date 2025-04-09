from collections import Counter
import heapq 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums) 
        return heapq.nlargest(k, count_dict.keys(), key=count_dict.get)
