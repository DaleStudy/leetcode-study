from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = [x for x in sorted(candidates) if x <= target]
        res = self.dfs(candidates, target, [], 0)

        return res

    def dfs(
        self, candidates: List[int], target: int,
        visited: List[int], prev_sum: int
    ) -> List[List[int]]:
        if prev_sum == target:
            return [visited]

        arr = []
        for i in range(len(candidates)):
            if prev_sum + candidates[i] > target:
                continue

            res = self.dfs(
                candidates[i:], target,
                visited + [candidates[i]], prev_sum + candidates[i]
            )
            for item in res:
                arr.append(item)

        return arr
