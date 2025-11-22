class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, current_sum):
            if current_sum == target:
                result.append(current[:])
                return

            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, current_sum + candidates[i])
                current.pop()

        backtrack(0, [], 0)
        return result


"""
================================================================================
풀이 과정
================================================================================

1. 이거 모든 가능한 조합을 찾아야하는데 합이 target을 넘으면 중단되야하네?
2. 문제는 같은 숫자를 여러 번 쓸 수 있는건데..
3. 백트래킹으로 접근해야할 것 같은데..


[1차 시도] 백트래킹 (Backtracking)
────────────────────────────────────────────────────────────────────────────────
4. 모든 조합을 탐색하되, 조건에 맞지 않으면 가지치기
5. 같은 숫자를 여러 번 사용할 수 있으므로 재귀 호출 시 같은 인덱스부터 시작
6. 중복 조합 방지를 위해 start 인덱스 사용

        result = []

        def backtrack(start, current, current_sum):
            # target을 만족하면 결과에 추가
            if current_sum == target:
                result.append(current[:])  # 복사해서 추가
                return

            # 가지치기: 합이 target 초과
            if current_sum > target:
                return

            # 조합 탐색
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                # 같은 숫자 재사용 가능하므로 i부터 시작
                backtrack(i, current, current_sum + candidates[i])
                current.pop()  # 백트래킹: 상태 복원

        backtrack(0, [], 0)
        return result

7. Example: candidates = [2,3,6,7], target = 7

   backtrack(0, [], 0)
   ├─ 2 추가 → backtrack(0, [2], 2)
   │  ├─ 2 추가 → backtrack(0, [2,2], 4)
   │  │  ├─ 2 추가 → backtrack(0, [2,2,2], 6)
   │  │  │  └─ 2 추가 → backtrack(0, [2,2,2,2], 8) → 8 > 7 return
   │  │  └─ 3 추가 → backtrack(1, [2,2,3], 7) → 7 == 7 ✅ [2,2,3]
   │  └─ 3 추가 → backtrack(1, [2,3], 5)
   │     └─ ... (탐색 계속)
   └─ 7 추가 → backtrack(3, [7], 7) → 7 == 7 ✅ [7]

8. 시간 복잡도: O(N^(T/M))
   - N: candidates 길이
   - T: target 값
   - M: candidates의 최소값
9. 공간 복잡도: O(T/M) - 재귀 호출 스택 깊이
"""