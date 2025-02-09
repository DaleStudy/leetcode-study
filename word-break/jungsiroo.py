class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP를 활용한 문제

        """
        KMP나 Rabin Karp를 이용하여 푸는 문제인 줄 알았으나 전혀 아닌 문제
        neetcode의 도움을 받았음
        
        계속 순회를 하면서 if dp[j]를 통해 길이만큼 끊어주고 word_set에 있는지를 확인함
        Time Complexity : O(n^2)
        Space Complexity : O(n)
        """
        
        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True  

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]

