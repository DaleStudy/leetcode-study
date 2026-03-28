class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def backtrack(remain, comb, start):
            if remain == 0:
                output.append(list(comb))
                return

            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i)
                comb.pop()

        backtrack(target, [], 0)
        return output

# Time Complexity : O(N^T/M) N - number of candidates, T - target, M - minimum value in candidates
# Space Complexity : O(T/M) - maximum depth of the recursion tree
