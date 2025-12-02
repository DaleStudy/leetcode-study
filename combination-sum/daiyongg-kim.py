class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtracking(start_index, current_combination, current_sum):
            if current_sum == target:
                result.append(list(current_combination))
                return

            if current_sum > target:
                return
            
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]

                if current_sum + candidate > target:
                    break
                
                current_combination.append(candidate)
                backtracking(i, current_combination, current_sum + candidate)

                current_combination.pop()
        
        backtracking(0, [], 0)
        return result
