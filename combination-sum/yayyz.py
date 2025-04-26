class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(path, total, start):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                dfs(path + [candidates[i]], total + candidates[i], i)

        dfs([], 0, 0)
        return result
