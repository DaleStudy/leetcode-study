from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return indices of two numbers such that they add up to target
        '''
        [Complexity]
        Time: O(n)
        Space: O(1)
        '''
        nums_dict = {}
        for idx, num in enumerate(nums):
            remaining = target - num
            if remaining in nums_dict:
                return [idx, nums_dict[remaining]]
            nums_dict[num] = idx
        '''
        [Complexity]
        Time: O(n^2)
        Space: O(1)

        for i in range(0,len(nums)-1):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
        '''
