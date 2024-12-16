# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert list to set to remove duplicates and allow quick lookups
        num_set = set(nums)
        longest_streak = 0

        # loop through each number in the set
        for num in num_set:
            # only start counting if it's the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # keep counting while the next number in the sequence exists
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # update the longest streak found so far
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
