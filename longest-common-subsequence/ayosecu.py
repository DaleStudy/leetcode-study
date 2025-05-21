class Solution:
    """
        - Time Complexity: O(mn), m = len(text1), n = len(text2)
        - Space Complexity: O(mn), The size of the dp variable
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [ [0] * (n + 1) for _ in range(m + 1) ]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    # if matched, increase length
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    # if unmatched, select a larger length from left and up position
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[m][n]


tc = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0) 
]

sol = Solution()
for i, (s1, s2, e) in enumerate(tc, 1):
    r = sol.longestCommonSubsequence(s1, s2)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
