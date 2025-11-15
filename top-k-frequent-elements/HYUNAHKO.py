class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        value_dict = {}
        
        for num in nums:
            if num in value_dict:
                value_dict[num] += 1
            else:
                value_dict[num] = 1
        
        sorted_items = sorted(value_dict.items(), key=lambda x: x[1], reverse=True)
        
        return [key for key, value in sorted_items[:k]]