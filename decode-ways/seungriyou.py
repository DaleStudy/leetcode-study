# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings1(self, s: str) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)

        [Approach]
            DP로 풀 수 있다.
            dp[i] = s[i]까지 봤을 때, 가능한 decoding 개수의 총합
                1) s[i] 한 자리만 가능한 경우: s[i] != 0
                   => dp[i] += dp[i - 1]
                2) s[i - 1:i + 1] 두 자리 모두 가능한 경우: 10 <= s[i - 1:i + 1] <= 26
                  => dp[i] += dp[i - 2]
            따라서, 초기 값으로 dp[0], dp[1]을 먼저 채워주어야 한다.
        """

        n = len(s)
        dp = [0] * n

        # early stop
        if s[0] == "0":
            return 0
        if n == 1:
            return 1

        # initialize (dp[0], dp[1])
        dp[0] = 1
        if s[1] != "0":
            dp[1] += dp[0]
        if 10 <= int(s[0:2]) <= 26:
            dp[1] += 1

        # iterate (dp[2] ~)
        for i in range(2, n):
            # 1) s[i] 한 자리만 가능한 경우
            if s[i] != "0":
                dp[i] += dp[i - 1]
            # 2) s[i - 1:i + 1] 두 자리 모두 가능한 경우
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]

    def numDecodings(self, s: str) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            O(n) space DP에서 매 단계에서 dp[i - 1], dp[i - 2] 두 값만 확인하므로, O(1) space로 space optimize 할 수 있다.
                dp[i - 1] = prev1
                dp[i - 2] = prev2
        """

        prev2, prev1 = 1, 1 if s[0] != "0" else 0

        for i in range(1, len(s)):
            curr = 0  # = dp[i]

            # 1) s[i] 한 자리만 가능한 경우
            if s[i] != "0":
                curr += prev1
            # 2) s[i - 1:i + 1] 두 자리 모두 가능한 경우
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                curr += prev2

            prev2, prev1 = prev1, curr

        return prev1
