class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[len(s)]


"""
================================================================================
풀이 과정
================================================================================

[문제 이해]
────────────────────────────────────────────────────────────────────────────────
1. 문자열 s와 사전 wordDict가 주어짐
2. s를 사전에 있는 단어들로 분할할 수 있는지 판단

    예시 1: s = "leetcode", wordDict = ["leet", "code"]
    → True ("leet" + "code")

    예시 2: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    → False (어떻게 나눠도 안 됨)


[접근 방법] DP
────────────────────────────────────────────────────────────────────────────────
3. dp[i] = s[0:i]를 사전 단어들로 분할 가능한가?

4. 점화식: dp[i] = dp[j] and s[j:i] in word_set (어떤 j에 대해)
   - dp[j]가 True이고, s[j:i]가 사전에 있으면 dp[i] = True

5. 예시: s = "leetcode"

      l  e  e  t  c  o  d  e
      0  1  2  3  4  5  6  7  8
   T  ?  ?  ?  T  ?  ?  ?  T
   │           │           │
   빈문자열    "leet"      "code"

   dp[4] = dp[0] + "leet" → True
   dp[8] = dp[4] + "code" → True


[복잡도 분석]
────────────────────────────────────────────────────────────────────────────────
6. 시간복잡도: O(n² × m)
   - n: 문자열 길이
   - m: 평균 단어 길이 (해시 비교)

7. 공간복잡도: O(n)
   - dp 배열 크기
"""
