"""
 * Time Complexity: O(N)
 * Space Complexity: O(N)
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for i, e in enumerate(nums):
            other = target - e
            if other in num_dict:
                return [num_dict[other], i]
            num_dict[e] = i
        return []
    