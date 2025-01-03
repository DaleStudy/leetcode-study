# 시간복잡도 : O(n * m) (n: target, m: len(candidates))
# 공간복잡도 : O(n * m)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        
        for candidate in candidates:
            for num in range(candidate, target + 1):
                for combination in dp[num - candidate]:
                    temp = combination.copy()
                    temp.extend([candidate])
                    dp[num].append(temp)

        return dp[target]
    
