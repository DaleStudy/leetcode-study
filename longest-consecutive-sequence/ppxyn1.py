# idea: - 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        return ans



'''
Trial and error

The code below was passed on Leecode since their Constraints was 0 <= nums.length <= 10^5.
But I realised that I missed another constraint they mentioned, which is "You must write an algorithm that runs in O(n) time."
'''
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if len(nums)==0:
#             return 0
#         sorted_nums = sorted(list(set(nums))) 
#         # sorted_nums = sorted(nums) # duplicate
#         max_len = 1
#         tmp = 1

#         for i in range(1, len(sorted_nums)):
#             if sorted_nums[i] == sorted_nums[i - 1] + 1:
#                 tmp += 1
#             else:
#                 max_len = max(max_len, tmp)
#                 tmp = 1 
#         ans = max(max_len, tmp)
#         return  ans



