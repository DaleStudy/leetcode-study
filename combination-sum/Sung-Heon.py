class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(start: int, target: int, current: list[int]):
            if target == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue

                current.append(candidates[i])
                backtrack(i, target - candidates[i], current)
                current.pop()

        candidates.sort()
        backtrack(0, target, [])
        return result
