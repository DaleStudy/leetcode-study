"""
시간 복잡도:
- 외부 루프는 O(n), 내부 루프는 최악의 경우 각 i에 대해 O(n)만큼 실행됩니다. (n: 문자열 s의 길이)
- s[j:i]를 wordSet에서 찾는 작업은 O(1)입니다 (set 사용).
- 전체 시간 복잡도: O(n^2).

공간 복잡도:
- DP 배열은 O(n)의 공간을 차지합니다.
- wordSet은 wordDict에 있는 모든 문자의 총 길이를 기준으로 O(m)의 공간을 차지합니다. (m: wordDict의 단어 수)
- 전체 공간 복잡도: O(n + m).
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]
