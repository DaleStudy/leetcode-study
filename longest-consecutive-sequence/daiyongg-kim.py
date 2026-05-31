class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0
        length = 1
        for num in my_set:
            if num - 1 not in my_set:
                length = 1
                while num + length in my_set:
                    length += 1
                longest = max (longest, length)

        return longest
