"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

개선 코드
O(N) time, O(N) space
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        
        for i, v in enumerate(nums):
            diff = target - v
            if diff in indices:
                j = indices[diff]
                return [i, j]
            indices[v] = i


"""
처음 풀이
O(N^2) time, O(N) space
"""

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         result = []
#         for i in range(len(nums)):
#             rest = target - nums[i]
#             rest_nums = nums[i+1:]
#             if rest in rest_nums:
#                 result.extend([i, rest_nums.index(rest)+i+1])
#                 break
#         return result
    

# JS 풀이
# /**
#  * @param {number[]} nums
#  * @param {number} target
#  * @return {number[]}
#  */
# var twoSum = function(nums, target) {
#     let indices = new Map();

#     for (let i = 0; i < nums.length; i++) {
#         diff = target - nums[i];
#         if (indices.has(diff)) {
#             return [i, indices.get(diff)];
#         }
#         indices.set(nums[i], i);
#     }
# };
