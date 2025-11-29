class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        n = len(s)
        # dp[i]를 i번쨰까지 처리했을떄의 경우의 수의 합으로 정의
        dp = [0] * n
        # dp[0] = 1 (첫자리 수)
        dp[0] = 1

        # i번쨰 숫자가 1~9로 대체될 수 있으면 이전까지의 경우의 수 합을 이어감
        # i번쨰 숫자(두자리수)가 10~26으로 대체될 수 있으면 앞자리는 사용한 것이므로 그 앞자리까지의 상태를 가져옴
        # 시간복잡도, 공간복잡도 O(n)
        for i in range(1, n):
            num1 = int(s[i])
            num2 = int(s[i -1 : i + 1])
            if 1 <= num1 <= 9:
                dp[i] += dp[i - 1]
            if 10 <= num2 <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[n-1]
