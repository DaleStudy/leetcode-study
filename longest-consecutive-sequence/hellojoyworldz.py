# - 문제: https://leetcode.com/problems/longest-consecutive-sequence/
# - 풀이: https://www.algodale.com/problems/longest-consecutive-sequence/

# Current complexity:O(NlogN)
# Suggested complexity:O(N)

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sorted_nums = sorted(set(nums))

        max_sequence = 1
        current_sequence = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - sorted_nums[i - 1] == 1:
                current_sequence += 1
                max_sequence = max(max_sequence, current_sequence)
            else:
                current_sequence = 1

        return max(max_sequence, current_sequence)

