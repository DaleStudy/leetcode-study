"""
# Intuition
backtracking

# Complexity
- Time complexity: N을 깊이만큼 곱한다. 따라서 아래와 같을 때, O(N^(T/M))
    N = candidates 개수
    T = target
    M = candidates 중 최소값

- Space complexity: O(T/M)
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer = []
        output = []

        def dfs(cur_i, cur_sum):
            if cur_sum == target:
                answer.append(output[:])
                return

            for i in range(cur_i, len(candidates)):
                num = candidates[i]

                if cur_sum + num > target:
                    break

                output.append(num)
                dfs(i, cur_sum + num)
                output.pop()

        dfs(0, 0)
        return answer
