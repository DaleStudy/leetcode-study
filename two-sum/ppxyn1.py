# idea: For each number n in nums, check if (target - n) exists in the remaining elements.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            required_num = target - num
            if required_num in nums[idx+1:]:
                return [idx, nums.index(required_num, idx+1)]


'''
Trial and error
idea : two pointer
I struggled to handle the indices of the original array after sorting it.
The code below fails when negative numbers are involved.
I realized it would be tricky to solve this problem with the two-pointer.
'''

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         sorted_nums = sorted(nums)
#         left, right = 0, len(nums) - 1
        
#         while left < right:
#             s = sorted_nums[left] + sorted_nums[right]
#             if s == target:
#                 left_idx = nums.index(sorted_nums[left])
#                 right_idx = nums.index(sorted_nums[right], left_idx + 1)
#                 return [left_idx, right_idx]
#             elif s < target:
#                 left += 1
#             else:
#                 right -= 1

