# O(n) time, O(n) space

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        
        for idx, num in enumerate(nums):
            other_num = target - num
            if other_num in num_set:
                return [idx, num_set[other_num]]
            else:
                num_set[num] = idx
