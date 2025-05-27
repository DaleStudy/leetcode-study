# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence_2d(self, text1: str, text2: str) -> int:
        """
        [Complexity]
            - TC: O(m * n)
            - SC: O(m * n)

        [Approach]
            dp[i][j] = text1[:i]와 text2[:j]의 longest common subsequence의 길이
                     = (text1[i - 1] == text2[j - 1] 라면) dp[i - 1][j - 1] + 1 (text1[:i - 1]와 text2[:j - 1]의 longest common subsequence 길이)
                       (text1[i - 1] != text2[j - 1] 라면) max(dp[i - 1][j], dp[i][j - 1])
        """
        m, n = len(text1), len(text2)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        [Complexity]
            - TC: O(m * n)
            - SC: O(n)

        [Approach]
            2D DP에서, 현재 row와 이전 row만 필요로 하기 때문에 1D DP로 space optimize 할 수 있다.
            dp[i]를 curr로, dp[i - 1]를 prev로 유지한다. (이때, curr와 prev는 len이 n + 1이다.)
        """
        m, n = len(text1), len(text2)

        prev = [0 for _ in range(n + 1)]
        curr = [0 for _ in range(n + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])

            # 다음 row로 넘어가기 위해 바꿔치기
            curr, prev = prev, curr

        return prev[-1]
