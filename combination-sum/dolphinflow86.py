class Solution:
    def backtrack(self, candidates: List[int], remain: int, start_index: int, path:List[int], answer: List[List[int]]):
        if remain == 0:
            answer.append(path[:])
            return

        cur = candidates[start_index]
        
        for i in range(start_index, len(candidates)):
            if remain < candidates[i]:
                break

            path.append(candidates[i])
            self.backtrack(candidates, remain - candidates[i], i, path, answer)
            path.pop()
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        answer = []

        candidates.sort()
        self.backtrack(candidates, target, 0, path, answer)
        
        return answer
