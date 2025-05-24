class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # DP (시간복잡도 : O(len(text1)*len(text2)), 공간복잡도 : O(len(text1)*len(text2)))
        # dp[i][j] : text1의 앞i글자와 text2의 앞j글자 사이의 LCS(가장긴공통부분수열)길이
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                
                #  현재 문자가 같다면, 이전 대각선 값에 +1
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                
                # 현재 문자가 다르다면, 왼쪽이나 위쪽 중 더 큰 값
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[len(text1)][len(text2)]
