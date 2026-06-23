class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}

        for idx, num in enumerate(nums):
            idx_map[num] = idx

        for idx, num in enumerate(nums):
            need = target - num

            if need in idx_map and idx != idx_map[need]:
                return [idx, idx_map[need]]

        return []
