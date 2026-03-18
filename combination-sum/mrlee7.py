from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, nums = list(), list()

        def dfs(start_position, total_sum):
            if total_sum > target:
                return
            if total_sum == target:
                result.append(nums[:])
            for idx in range(start_position, len(candidates)):
                num = candidates[idx]
                nums.append(num)
                dfs(idx, total_sum + num)
                nums.pop()

        dfs(0, 0)
        return result
