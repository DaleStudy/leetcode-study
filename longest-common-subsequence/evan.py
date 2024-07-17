class Solution:
    def longestCommonSubsequence(self, text1, text2):
        text1_length, text2_length = len(text1), len(text2)
        # dp[i][j]는 text1의 처음 i 글자와 text2의 처음 j 글자의 LCS 길이를 의미합니다.
        dp = [[0] * (text2_length + 1) for _ in range(text1_length + 1)]

        for text1_char in range(1, text1_length + 1):
            for text2_char in range(1, text2_length + 1):
                if text1[text1_char - 1] == text2[text2_char - 1]:
                    # 두 문자가 같으면 그 이전까지의 LCS 길이에 1을 더한 값으로 현재 위치를 갱신합니다.
                    dp[text1_char][text2_char] = dp[text1_char - 1][text2_char - 1] + 1
                else:
                    # 두 문자가 다르면 이전까지의 최대 LCS 길이 중 더 큰 값을 현재 위치에 저장합니다.
                    dp[text1_char][text2_char] = max(
                        dp[text1_char - 1][text2_char], dp[text1_char][text2_char - 1]
                    )

        return dp[text1_length][text2_length]
