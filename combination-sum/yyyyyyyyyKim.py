class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        answer = []
        
        # 재귀
        def backtrack(start, path, total):
            # total이 target과 같아지면 path복사해서 answer에 추가하고 종료
            if total == target:
                answer.append(path[:])
                return

            # total이 target값 넘어가면 종료
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])  # 일단 path에 추가하고
                backtrack(i, path, total + candidates[i])   # 검증하기
                path.pop()  # 마지막 값 꺼내고 다음으로

        # backtrack 함수호출
        backtrack(0, [], 0)

        return answer
