"""
Solution:
    최초 풀이 당시엔 단순히 dfs로 풀었으나 시간 초과로 실패했습니다.
    이후 풀이 설명을 통해 i 번째 숫자를 넣거나 / 안넣거나 라는 조건으로 i를 늘려가도록 진행하는 백트래킹을 하면 된다는점을 배웠습니다. 
    이를 통해 불필요한 중복을 줄이고 효율적인 구현이 가능해집니다.

C: len(candidates)
T: target size

Time: O(C^T) = 라고 설명되어 있는데 솔찍히 잘 모르겠습니다.
Space: O(T) = 재귀가 가장 깊을 때 [1,1,1,1...] T 만큼이기 때문에 O(T)
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sol = []
        n = len(candidates)

        def backtrack(i, cur_sum):
            if cur_sum == target:
                result.append(sol.copy())
                return
            if cur_sum > target or i == n:
                return

            backtrack(i + 1, cur_sum)

            sol.append(candidates[i])
            backtrack(i, cur_sum + candidates[i])
            sol.pop()

        backtrack(0, 0)
        return result
