class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_list = {}
        for num in nums:
            if num not in num_list:
                num_list[num] = 1
            else:
                num_list[num] += 1
        
        return [n[1] for n in sorted([[num_list[key], key] for key in num_list.keys()], reverse=True)[:k]]
    