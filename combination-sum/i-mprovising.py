"""
Time complexity O(c*t)
Space complexity O(c*t)

Dynamic programming
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # init dp array
        dp = [[] for _ in range(target+1)] # dp[i] : combinations to sum to i
        dp[0] = [[]]

        for candidate in candidates:
            for num in range(candidate, target+1):
                for comb in dp[num-candidate]:
                    dp[num].append(comb + [candidate])
        
        return dp[-1]
