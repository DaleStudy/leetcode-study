"""
시간 복잡도 O(N)
공간 복잡도 O(N)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0

        for i in nums_set:
            if i - 1 not in nums_set:
                length = 1
                while i + length in nums_set:
                    length += 1
                result = max(result, length)
        
        return result
