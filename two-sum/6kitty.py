#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            for j in range(i+1,len(nums)):
                if num + nums[j] == target:
                    return [i,j]
        
# @lc code=end

