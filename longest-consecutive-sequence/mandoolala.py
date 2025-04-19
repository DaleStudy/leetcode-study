from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in num_set:
                cnt = 1
                next_num = num + 1
                while next_num in num_set:
                    cnt += 1
                    next_num += 1
                longest = max(longest, cnt)
        return longest
