"""
시간 복잡도: O(target * n)
공간 복잡도: O(n)?
개인적으로 어려웠던 문제라서 정답을 봤습니다.
추후에 다시 복습할 예정입니다.
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for candidate in candidates:
            for num in range(candidate, target + 1):
                for combination in dp[num - candidate]:
                    dp[num].append(combination + [candidate])
        return dp[target]
