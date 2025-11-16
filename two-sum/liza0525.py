class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {
            num: idx
            for idx, num in enumerate(nums)
        }

        for idx, num in enumerate(nums):
            result_num = target - num 
            if result_num in idx_map and idx != idx_map[result_num]:
                return [idx, idx_map[result_num]]
