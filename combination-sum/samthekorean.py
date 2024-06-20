# TC : O(n^2)
# SC : O(n)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(start: int, total: int, current_combination: List[int]):
            if total > target:
                return
            if total == target:
                result.append(current_combination[:])
                return
            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                dfs(i, total + candidates[i], current_combination)
                current_combination.pop()

        dfs(0, 0, [])
        return result
