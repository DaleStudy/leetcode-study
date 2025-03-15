# Time Complexity: O(n) -> iterate through the houses twice, each in O(n) time.
# Space Complexity: O(1) -> use a few extra variables, no additional data structures.

class Solution:
    def rob(self, nums: List[int]) -> int:        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # track the max money from two houses before and last house.
        var1, var2 = 0, 0  
        
        # robbing from first house to second-last house (excluding last house)
        for i in nums[:-1]:
            # store previous max before updating.
            temp = var1  
            # either rob this house or skip it.
            var1 = max(var2 + i, var1)  
            # move to the next house.
            var2 = temp  
        
        # same logic, but robbing from second house to last house.
        vaar1, vaar2 = 0, 0  
        
        for i in nums[1:]:
            temp = vaar1
            vaar1 = max(vaar2 + i, vaar1)
            vaar2 = temp
        
        # take the max of both cases.
        return max(var1, vaar1)  
