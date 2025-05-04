class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # DP
        dp = [False]*(len(s)+1)
        dp[0] = True    # 빈문자열은 단어없이도 만들 수 있음(True)

        # i : s의 i번째 문자
        for i in range(1,len(s)+1):
            # j : 단어 자르는 시작위치. s[:j]가 wordDict에 있고, s[j:i]가 wordDict에 있는지 확인.
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True    # s[i]까지 자를 수 있음(True)
                    break   # 자를 수 있으니까 더 볼 필요 없음

        return dp[len(s)]
