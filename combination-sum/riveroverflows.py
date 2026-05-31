class Solution:
    """
    TC: O(N^(T/M))
        - N = len(candidates), T = target, M = min(candidates)
    SC: O((T/M) * N^(T/M))

    풀이:
    백트래킹으로 모든 조합을 탐색하되, 중복 조합 방지를 위해
    start 인덱스를 활용하여 이전 후보는 건너뛰고, 같은 후보는 재사용 허용.
    path_sum > target이면 가지치기(pruning)하여 불필요한 탐색을 줄임.
    """
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        answer = []

        def backtrack(start, path, path_sum):
            if path_sum > target:
                return

            if path_sum == target:
                answer.append(path[:])
                return

            for i in range(start, len(candidates)):
                candidate = candidates[i]
                path.append(candidate)
                path_sum += candidate
                backtrack(i, path, path_sum)
                path_sum -= candidate
                path.pop()

        backtrack(0, [], 0)

        return answer
