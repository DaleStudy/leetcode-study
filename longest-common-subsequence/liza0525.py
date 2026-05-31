# 7기 풀이
# 시간 복잡도: O(n * m)
# - text1의 길이 n과 text2의 길이 m만큼 순회하며 계산함
# 공간 복잡도: O(n * m)
# - text1의 길이 n과 text2의 길이 m만큼의 2차 배열을 만들어 DP 계산을 하기 때문
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [
            [0 for _ in range(len(text2) + 1)]
            for _ in range(len(text1) + 1)
        ]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    # text1의 i번째 문자와 text2의 j번째 문자가 같다면
                    # 이 문자는 공통 subsequence에 포함될 수 있으므로
                    # 두 문자를 제외한 나머지(dp[i-1][j-1])에 1을 더한 값이 현재의 LCS 길이가 된다
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 같지 않다면 둘 중 하나를 제외했을 때의 LCS 중 더 큰 값을 가져온다
                    # dp[i][j-1]: text2의 j번째 문자를 제외한 경우
                    # dp[i-1][j]: text1의 i번째 문자를 제외한 경우
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]
