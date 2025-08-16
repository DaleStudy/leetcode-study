class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Time complexity: O(n ^ (T / m))
        result = []

        def dfs(remain_sum, index, path):
            if remain_sum < 0:
                return
            if remain_sum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(remain_sum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result
