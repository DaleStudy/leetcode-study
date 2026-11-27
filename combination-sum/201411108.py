#TC: O(n log n), candidates의 리스트를 기준으로, 재귀 호출을 통해서 조합 확인
#SC: O(n), result에 최대 n개의 조합이 들어갈 수 있음
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        
        sorted_candidates = candidates[:]
        sorted_candidates.sort()

        def explore(path: list[int], diff: int, start_index: int):
            if diff == 0:
                result.append(path[:])
                return

            for i in range(start_index, len(sorted_candidates)):
                cur = sorted_candidates[i]

                path.append(cur)
                
                if diff < cur:
                    path.pop()
                    continue
                
                explore(path, diff - cur, i)
                path.pop()
        
        explore([], target, 0)
        return result

