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
    

"""
개선 코드
O(N) time, O(N) space
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        
        for i, v in enumerate(nums):
            diff = target - v
            if diff in indices:
                j = indices[diff]
                return [i, j]
            indices[v] = i

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