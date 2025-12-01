# // Input: candidates = [2,3,5], target = 8
# // Output: [[2,2,2,2],[2,3,3],[3,5]]

# // DFS/backtracking should be used - Find possilbe combinations till the end and backtrack to previous step to find other combinations
# // For example, if we have candidates [2,3,5] and target 8
# // Start with empty combination [], target 8
# // Add 2 -> [2], remaining 6
# // Add 2 -> [2,2], remaining 4
# // Add 2 -> [2,2,2], remaining 2
# // Add 2 -> [2,2,2,2], remaining 0 (found a valid combination)
# // Backtrack to [2,2,2,3], remaining -1 (remaining is negative, backtrack)
# // Backtrack to [2,2,2,5], remaining -3 (remaining is negative, backtrack)
# // Backtrack to [2,2,3], remaining 1 (dead end, backtrack)
# // Backtrack to [2,2,5], remaining -3 (remaining is negative, backtrack)
# // Backtrack to [2,3], remaining 3
# // Add 3 -> [2,3,3], remaining 0 (found a valid combination)
# // so on ..

# // When you dfs, always start from current index and allow reusing the same element or next index only to avoid duplicates / to get unique combination
# // Hence, if we starts from 2, next dfs calls can start from index of 2 or index of 3, but not index of 5 directly
# // Moreover, if we start from 3, next dfs calls can start from index of 3 or index of 5, but not index of 2 directly



from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result: List[List[int]] = []

        def backtrack(remaining: int, combination: List[int], start_index: int):
            # base cases
            if remaining == 0:
                # append a COPY of combination
                result.append(combination[:])
                return
            if remaining < 0:
                return

            # try candidates from start_index onward
            for i in range(start_index, len(candidates)):
                current_number = candidates[i]
                # choose
                combination.append(current_number)
                # explore (i, not i+1, because we can reuse same element)
                backtrack(remaining - current_number, combination, i)
                # undo (backtrack)
                combination.pop()

        # initial call
        backtrack(target, [], 0)
        return result
        


        
        