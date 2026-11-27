"""
N: candidates의 개수
D: target // min(candidates) (최대 재귀 깊이)
K: 정답 조합의 개수

TC : O(N log N + N^D + K * D)
- 정렬: O(N log N)
- 탐색: 최대 N개 선택, 깊이 D -> O(N^D)
- 결과 복사: O(K * D)

SC: O(N + D + K * D)
- 정렬 보조 공간: O(N)
- 재귀 스택 및 picked: O(D)
- 결과 저장: O(K * D)
"""
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        candidates.sort()
        ans = []

        def backtrack(picked, start, curr_sum):
            if curr_sum == target:
                ans.append(picked[:])
                return
            for i in range(start, n):
                if curr_sum + candidates[i] > target:
                    break
                picked.append(candidates[i])
                backtrack(picked, i, curr_sum + candidates[i])
                picked.pop()

        backtrack([], 0, 0)

        return ans
