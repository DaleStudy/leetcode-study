"""
Conditions:
- 1 <= s.length <= 100
- s contains only digits and may contain leading zero(s).

Time Complexity: O(n)
- 각 문자를 한 번씩만 방문함 (문자열의 길이: n)

Space Complexity: O(n)
- dp 배열의 크기는 n+1
- 이 배열 이외에 추가 공간을 사용하지 않음

Base cases:
- If string is empty or starts with '0', return 0 (impossible to decode)

Dynamic Programming approach:
- dp[i] represents the number of ways to decode first i characters
- dp array has size n+1 to include the empty string case (dp[0])
- For each position, consider both single-digit and two-digit decodings

메모:
- 다른 dp문제 풀어보기
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            if i > 1 and s[i-2] != '0':
                two_digit = int(s[i-2:i])
                if 1 <= two_digit <= 26:
                    dp[i] += dp[i-2]

        return dp[n]
