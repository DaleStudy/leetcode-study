from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dic = {num: idx for idx, num in enumerate(nums)}
        for i in range(len(nums)):
            remain = target - nums[i]
            exists_idx = nums_dic.get(remain)
            if exists_idx and exists_idx != i:
                return i, exists_idx
