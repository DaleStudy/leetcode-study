class Solution(object):
    def longestConsecutive(self, nums):

        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                max_length = max(max_length, length)

        return max_length


