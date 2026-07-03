# 1) Using modified bucket sort approach.  
# TC: O(N) where N is the length of nums
# SC: O(N) where N is the length of nums
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        bucket_count = len(nums)
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1 

        buckets = [[] for i in range(bucket_count + 1)]

        for num, freq in freq_map.items():
            buckets[freq].append(num)

        top_list = []
        for i in range(bucket_count, -1, -1):
            for num in buckets[i]:
                top_list.append(num)
                if len(top_list) == k:
                    return top_list
