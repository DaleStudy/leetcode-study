from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert to set for O(1) lookups
        num_set = set(nums)
        longest_length = 0

        for num in num_set:
            # Only start counting if num is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # Count the length of the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                longest_length = max(longest_length, current_length)
        
        return longest_length
