class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest = 0

        visited = set()

        for num in num_set:
            if num not in visited and num - 1 not in num_set:
                current = num
                current_streak = 0
                while current in num_set:
                    visited.add(current)
                    current_streak += 1
                    current += 1
                longest = max(longest, current_streak)

        return longest