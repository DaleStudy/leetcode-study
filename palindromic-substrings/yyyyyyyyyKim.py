class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # DP
        dp = [[False]*(len(s)) for _ in range(len(s))]  # dp 테이블 초기화(dp[i][j]=s[i:j+1]의 팰린드롬 여부)
        answer = 0

        # j = 끝글자인덱스, i = 처음글자인덱스
        for j in range(len(s)):
            for i in range(j+1):
                # 1. s[i](첫글자)와 s[j](끝글자)가 같은 글자이고,
                # 2. j-i <= 2, 즉 글자 길이가 1~3일때는 무조건 팰리드롬 /아니면 s[i+1][j-1](가운데글자들)이 팰린드룸이면 s[i]부터 s[j]까지 팰린드룸.  
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True # s[i]에서 s[j]는 팰린드룸(True)
                    answer += 1

        return answer
