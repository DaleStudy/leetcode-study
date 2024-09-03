# 시간복잡도: O(N^M)
# 공간복잡도: O(M)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(total, idx, path):
            if total < 0:
                return
            elif total == 0:
                res.append(path[:])

            for i in range(idx, len(candidates)):
                dfs(total - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])

        return res
