class Solution(object):
    def twoSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        
        for i, v in enumerate(nums):
            complement = target - v

            if complement in dic:
                return [i, dic[complement]]
            
            dic[v] = i
