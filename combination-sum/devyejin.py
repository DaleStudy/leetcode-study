class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        def backtracking(start, total, result):
            if total == target:
                answer.append(result[:])
                return

            if sum(result) > target:
                return

            for i in range(start, len(candidates)):
                result.append(candidates[i])
                backtracking(i, total + candidates[i], result)
                result.pop()

        answer = []
        backtracking(0, 0, [])
        return answer

