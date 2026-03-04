class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for n in nums:
            if n in table:
                table[n] += 1
            else:
                table[n] = 1
        sorted_table = sorted(table.items(), key=lambda x:x[1], reverse = True)
    
        return [ key for key, freq in sorted_table[:k]]
    