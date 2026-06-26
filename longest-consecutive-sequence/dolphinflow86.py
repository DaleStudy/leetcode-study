# Calculate the length of the streak from its starting point.
# TC: O(N) where N is the size of nums
# SC: O(N) where N is the size of nums
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert list to set for O(1) lookups
        num_set: Set[int] = set(nums)
        max_streak = 0

        for num in num_set:
            if num - 1 in num_set:
                continue
            
            # found streak starting point
            streak = 0
            cur_num = num

            # extend the streak as long as consecutive numbers exists
            while cur_num in num_set:
                streak += 1
                cur_num += 1
            
            # update max streak
            max_streak = max(streak, max_streak)

        return max_streak
