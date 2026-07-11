class Solution:
    def numDecodings(self, s: str) -> int:
        # invalid case
        if s[0] == "0":
            return 0

        dp = [0] * (len(s)+1)  # 앞에서부터 i개 문자를 해석하는 방법        
        
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s)+1):
            one_digit = s[i-1]
            two_digits = int(s[i-2]) * 10 + int(s[i-1])
            if one_digit != '0': # 현재 숫자를 한자리로 해석하는 경우. (0 은 매칭되는 알파벳이 없으므로 제외)
                dp[i] += dp[i-1]

            if 10 <= two_digits <= 26: # 현재 숫자를 바로 앞자리 숫자와 묶어서 두자리로 해석하는 경우 
                dp[i] += dp[i-2]
         
        return dp[len(s)]