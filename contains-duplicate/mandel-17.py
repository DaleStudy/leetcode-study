from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        stack_list = []
        for i, n in enumerate(nums[:-1]):
            stack_list.append(n)
            if nums[i+1] in stack_list:
                return True
            else:
                if i == len(nums[:-2]):
                  return False
                continue
            