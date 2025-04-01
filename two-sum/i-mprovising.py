"""
hash table
O(n) complexity
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {num:idx for idx, num in enumerate(nums)}
        for i, x in enumerate(nums):
            y = target - x
            if (y in table) and table[y] != i:
                return [i, table[y]]
