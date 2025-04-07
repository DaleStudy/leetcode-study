"""
Time complexity O(n)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # hash table
        longest = 0
        
        for n in num_set:
            if n-1 in num_set:
                continue
            cur_len = 1
            while n + cur_len in num_set:
                cur_len += 1

            longest = max(longest, cur_len)
        
        return longest
