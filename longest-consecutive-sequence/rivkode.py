class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in num_set:
                continue
            
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(length, longest)
        return longest
        


        