class Solution(object):
    # Time complexity: O(n) to generate set and O(n) to pop all items from set -> O(n) + O(n) = O(n)

    # create set from nums
    # pop one number and calculate length with neighbors
    # update longest_consivutive if the calculated length is bigger than existing number.
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start_dict = {}
        
        my_set = set(nums)
        longest_consicutive = 0

        while len(my_set):
            num = my_set.pop()
            length = 1
            start = num-1
            while start in my_set:
                my_set.remove(start)
                length += 1
                start -= 1
            end = num+1
            while end in my_set:
                my_set.remove(end)
                length += 1
                end += 1
            if length > longest_consicutive:
                longest_consicutive = length
        
        return longest_consicutive
            