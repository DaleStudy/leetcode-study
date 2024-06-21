class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for i in range(target + 1)]
        dp[0] = [[]]

        for num in candidates:
            for i in range(num, target + 1):
                for comb in dp[i - num]:
                    dp[i].append(comb + [num])

        return dp[target]

        ## TC: O(outer loop * 1st inner(target size) * 2nd inner(combination #))
        ## SC: O(target size * combination #)
