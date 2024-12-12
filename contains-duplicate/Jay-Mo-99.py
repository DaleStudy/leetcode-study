class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #??
        #sets don't allow duplicate elements.
        #If the length of the set created from nums is different from the original list(nums), It means there are duplicates. 
        
        #Big O
        #N: ??? ?? nums? ??(Length of the input list nums)
        #
        #Time Complexity: O(N)
        #- set? nums? ?? n? ???? ????(Creating a set from nums): O(N)
        #- ??? list? ?? nums?? ??? ??(Comparing the lengths between created list and original list) : O(1)
        #
        #Space Complexity: O(N)
        #-set? nums? ??? ?? ????? n? ????(The set requires extra space depends on the size of nums) : O(N) 
        if len(list(set(nums))) == len(nums): 
            return False
        else:
            return True