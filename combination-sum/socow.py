"""
        문제 요약
        - candidates 배열에서 숫자를 무제한 사용하여 합이 target이 되는 모든 조합 찾기

        아이디어
        - 백트래킹: i번째 인덱스부터 탐색하여 중복 조합 방지
        - 같은 숫자 재사용 가능 → 재귀 시 인덱스 i 유지
        - 정렬 후 target 초과 시 break로 가지치기

        시간복잡도: O(N^(T/M)) - N: candidates 길이, T: target, M: 최소값
        공간복잡도: O(T/M) - 재귀 깊이
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sol = []
        candidates.sort()
        n = len(candidates)

        def backtrack(start, cur_sum):
            if cur_sum == target:
                result.append(sol.copy())
                return

            for i in range(start, n):
                if cur_sum + candidates[i] > target:
                    break
                sol.append(candidates[i])
                backtrack(i, cur_sum + candidates[i])
                sol.pop()

        backtrack(0, 0)
        return result
