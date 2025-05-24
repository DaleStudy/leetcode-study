"""
두 문자열 text1, text2가 주어졌을 때, 순서를 유지하는 공통 부분 수열 중 가장 긴 길이를 반환해라 
- 없으면 0 반환
- 순서는 일치해야 하지만, 문자열 삭제 가능
- 소문자로만 이루어져 있음.
-  1 <= text1.length, text2.length <= 1000

# LCS DP 풀이
- dp[i][j]: 문자열 text1[:i]와 text2[:j]까지의 LCS 길이

1. text1[i - 1] == text2[j - 1], 두 문자열이 같은 경우
    LCS 길이 증가
    dp[i][j] = dp[i - 1][j - 1] + 1
2. 다른 경우
    text1[0...i] 또는 text2[0...j] 중 하나를 줄인 LCS 중 더 긴 쪽 선택
    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


TC: O(m * n)
SC: O(m * n)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 0번째 인덱스를 비워둬서 문자열이 ""일 때를 기본값으로 처리

        for i in range(1, m + 1):  # text1의 1 ~ m 인덱스
            for j in range(1, n + 1):  # text2의 1 ~ n 인덱스
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1  # 두 문자가 같으면, 이전 상태 + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 다르면, 하나 줄인 상태 중 최댓값 선택
        return dp[m][n]
