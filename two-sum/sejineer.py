"""
시간 복잡도 O(n)
공간 복잡도 O(n)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, v in enumerate(nums):
            x = target - v
            if x in nums_map:
                j = nums_map[x]
                return [j, i]
            nums_map[v] = i