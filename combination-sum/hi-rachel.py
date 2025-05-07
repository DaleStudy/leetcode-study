# DFS + 백트래킹
# 중복 조합 문제
# O(2^t) time, O(재귀 깊이 (t) + 결과 조합의 수 (len(result))) space

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums, result = [], []
        def dfs(start, total):
            if total > target:
                return
            if total == target:
                result.append(nums[:])
            for i in range(start, len(candidates)):
                num = candidates[i]
                nums.append(num)
                dfs(i, total + num)
                nums.pop()

        dfs(0, 0)
        return result
