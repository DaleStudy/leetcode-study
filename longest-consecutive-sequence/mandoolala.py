from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 in num_set:
                continue
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(length, longest)
        return longest
