
"""
Time Complexity: O(N^target)
Space Complexity: O(target)

Classic backtracking approach.
- Use a helper function to backtrack and generate all possible combinations.
"""
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         N = len(candidates)
#         candidates.sort()
        
#         ans = []
#         app = []

#         def backtracking(last: int, left: int) -> None:
#             if left == 0:
#                 ans.append(app[:])
#                 return

#             for i in range(last, N):
#                 if candidates[i] > left:
#                     continue

#                 app.append(candidates[i])
#                 backtracking(i, left - candidates[i])
#                 app.pop()

#         backtracking(0, target)

#         return ans

"""
Time Complexity: O(N * target)
Space Complexity: O(target)

- Use a dynamic programming approach to store the combinations that sum to each target.
- dp[j] is a list of lists that sum to j.
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [list() for _ in range(target + 1)]
        dp[0] = [[]]

        for c in candidates:
            for j in range(c, target + 1):
                for partial in dp[j - c]:
                    dp[j].append(partial + [c])

        return dp[-1]
