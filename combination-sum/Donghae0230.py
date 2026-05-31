# 문제 풀이
# 모든 경우의 수를 탐색하기 위해 백트래킹 사용
# - 현재 조합의 합이 target보다 크면 종료
# - 현재 조합의 합이 target과 같으면 결과에 추가

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, combination):
            if sum(combination) > target:
                return
            if sum(combination) == target:
                result.append(combination[:]) 
                return 
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(i, combination)
                combination.pop()
            
        result = []
        backtrack(0, [])
        return result
