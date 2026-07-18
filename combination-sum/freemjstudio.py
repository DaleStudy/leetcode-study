class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def backtracking(start_idx, total, path):
            if target == total:
                answer.append(path[:]) # 새로운 리스트 객체를 만들어서 저장함.
                # 리스트가 mutable 객체이므로 path[:] 로 복사하지 않으면 path 가 바뀔 때 answer 안의 값도 바뀌게 된다.
                return

            if target < total:
                return

            for idx in range(start_idx, len(candidates)):
                new_node = candidates[idx] # 동일한 숫자 재사용 가능함. start_idx 도 포함한다.
                path.append(new_node)

                backtracking(idx, total + new_node, path)
                # 선택 취소
                path.pop()

        backtracking(0, 0, [])
        return answer
