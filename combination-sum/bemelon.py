class Solution:
    # Space complexity: O(n)
    #  - n: len(candidates)
    #  - Stack Frame -> O(n) 
    #  - list_of_combination -> O(n) ? 
    # Time complexity: O(n!)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        list_of_combination = [] 
        n = len(candidates)
        
        def backtracking(curr: int, curr_combination: List[int], curr_sum: int): 
            if curr_sum == target:  # 목표값에 도달했을 경우
                list_of_combination.append(list(curr_combination))
                return
            
            if curr_sum > target:  # 목표값을 초과한 경우
                return
            
            for i in range(curr, n):
                curr_combination.append(candidates[i])
                backtracking(i, curr_combination, curr_sum + candidates[i])
                curr_combination.pop()  # 백트래킹 과정에서 마지막 요소 제거
        
        backtracking(0, [], 0)
        return list_of_combination
