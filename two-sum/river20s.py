class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return seen[comp], i
            if num not in seen:
                seen[num] = i
        return None

