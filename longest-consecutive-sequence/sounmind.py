from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time Complexity: O(n) where n is the length of nums
        # Strategy: Use a set for O(1) lookups and only extend sequences from their starting points
        if not nums:
            return 0

        max_streak = 0
        num_set = set(nums)

        # Only check sequences from their starting points to avoid redundant work
        for num in num_set:
            current_streak = 0

            # Check if this number is the start of a sequence (no left neighbor)
            if num - 1 not in num_set:
                # Found a sequence start - extend it as far as possible
                current_num = num

                while current_num in num_set:
                    current_streak += 1
                    current_num += 1

                # Update the longest streak found so far
                max_streak = max(max_streak, current_streak)

        return max_streak
