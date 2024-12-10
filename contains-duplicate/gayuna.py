class Solution(object):
    # Time complexity: O(n)

    # Iterate through all numbers.
    # if there is same number in set, early return with True.
    # if not exist, add the number to the set.
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_set = set()
        for i in nums:
            if i in my_set:
                return True
            my_set.add(i)
        
        return False