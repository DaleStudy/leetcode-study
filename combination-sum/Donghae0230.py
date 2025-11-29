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

