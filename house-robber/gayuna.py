class Solution(object):
    """
    the robber will have 2 choices for each house
    1. include this house for target and skip next one
    2. bypass this house.
    from house 1 to n, repeat this choice and use memoization for maximum money until the end to prevent duplicate calculation.

    time complexity: O(n) (forward iterating only)
    """
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_dict = {}
        def process(idx): # -> maximum
            if idx >= len(nums):
                return 0
            
            include_sum = nums[idx] + (my_dict[idx+2] if idx+2 in my_dict else process(idx+2))
            exclude_sum = my_dict[idx+1] if idx+1 in my_dict else process(idx+1)
            my_dict[idx] = max(include_sum, exclude_sum)
            return my_dict[idx]
        
        return process(0)
            
        