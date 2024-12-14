class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = {}
        
        for num in nums:
            if counters.get(num):
                counters[num] += 1
            else:
                counters[num] = 1
        
        return [val[0] for val in sorted(counters.items(), key=lambda x: x[1], reverse=True)[:k]]

