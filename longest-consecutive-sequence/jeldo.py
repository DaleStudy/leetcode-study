class Solution:
    # O(n)
    def longestConsecutive(self, nums: list[int]) -> int:
        max_length = 0
        nums_set = set(nums)
        for n in nums_set:
            if n - 1 not in nums_set:
                length = 0
                while n + length in nums_set:
                    length += 1
                    max_length = max(max_length, length)

        return max_length
