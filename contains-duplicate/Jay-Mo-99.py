class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #sets don't allow duplicate elements.
        #If the length of the set created from nums is different from the original list(nums), It means there are duplicates. 
        if len(list(set(nums))) == len(nums): 
            return False
        else:
            return True