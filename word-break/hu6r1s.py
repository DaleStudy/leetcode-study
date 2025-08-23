class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)   # O(1) 조회를 위해 set으로 변환
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True   # 공집합은 항상 가능

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break   # i번째까지 나눌 수 있으면 더 확인할 필요 없음

        return dp[-1]
