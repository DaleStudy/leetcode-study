'''
# 213. House Robber II

house roober 1 + circular array

## Solution
solve by using two cases:
- robbing from the first house to the last house
- robbing from the second house to the last house
'''
class Solution:
    '''
    A. pass indices to function
    TC: O(n)
    SC: O(1)
    '''
    def rob(self, nums: Lit[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robbing(start, end):
            prev, maxAmount = 0, 0

            for i in range(start, end):
                prev, maxAmount = maxAmount, max(maxAmount, prev + nums[i])
            
            return maxAmount

        return max(robbing(0, len(nums) - 1), robbing(1, len(nums)))

    '''
    B. pass list to function
    TC: O(n)
    SC: O(n) (list slicing)
    '''
    def robWithSlicing(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robbing(nums):
            prev, maxAmount = 0, 0

            for num in nums:
                prev, maxAmount = maxAmount, max(maxAmount, prev + num)
            
            return maxAmount

        return max(robbing(nums[1:]), robbing(nums[:-1]))
