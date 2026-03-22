# https://leetcode.com/problems/combination-sum/

# for문으로 해결이 되지 않아 gpt 도움을 받아 해결하였습니다.
# 같은 숫자를 재사용하면서, 순서를 고정해서 중복 없는 조합을 DFS로 탐색하는 구조
# 시간 복잡도 : O(2^n) (백트래킹 탐색)
# 공간 복잡도 : O(target) (재귀 깊이)

class Solution(object):
    def combinationSum(self, candidates, target):
        
        result = []

        def dfs(start, path, total):
            # 종료 조건 1 : target을 맞춘 경우
            if total == target:
                result.append(path[:])
                return
            
            # 종료 조건 2 : target 초과한 경우
            if total > target:
                return
            
            # 후보 탐색 -> 같은 방향으로만 탐색
            for i in range(start, len(candidates)):
                # 같은 숫자 재사용 가능 -> i를 그대로 넘기기
                dfs(i, path+[candidates[i]], total+candidates[i])   # 새로운 리스트 만들어서 전달
            
        
        dfs(0, [], 0)

        return result
