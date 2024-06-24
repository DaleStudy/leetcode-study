"""
39. Combination Sum
https://leetcode.com/problems/combination-sum/

Solution
    To solve this problem, we can use backtracking.
    The idea is to explore all possible combinations starting from each candidate.
    
    - We can sort the candidates to avoid duplicates.
    - We can create a helper function that takes the remaining target, the current combination, and the start index.
    - If the remaining target is 0, we have found a valid combination, so we add it to the result.
    - If the remaining target is negative, we return.
    - We iterate through the candidates starting from the start index.
    - We add the current candidate to the combination and recursively call the helper function with the updated target and combination.
    - After the recursive call, we remove the current candidate from the combination.

Time complexity: O(2^n)
    - In the worst case, we explore all possible combinations.
    - For each candidate, we have two choices: include it or exclude it.

Space complexity: O(n)
    - The recursive call stack has a maximum depth of n.
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remain, comb, start):
            if remain == 0:
                result.append(list(comb))
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                current_candidate = candidates[i]
                if current_candidate > remain:
                    break

                comb.append(current_candidate)
                backtrack(remain - current_candidate, comb, i)
                comb.pop()

        candidates.sort()
        result = []
        backtrack(target, [], 0)
        return result
