# 6기 
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         prevMap = {} # val : index 
#         for i, n in enumerate(nums):
#             diff = target - n 
#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[n] = i 

# 7기 
# https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use Hash map to save num and index 
        nums_hm = {}

        for i, num in enumerate(nums):
            find_val = target - num

            if find_val in nums_hm:
                return [nums_hm[find_val], i]

            nums_hm[num] = i
