# 문제: https://leetcode.com/problems/climbing-stairs/
# 해설: https://www.algodale.com/problems/climbing-stairs/
# 위치: https://github.com/DaleStudy/leetcode-study/tree/main/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        prev2, prev1 = 1, 1
        for _ in range(n - 1):
            prev2, prev1 = prev1, prev2 + prev1
        return prev1

