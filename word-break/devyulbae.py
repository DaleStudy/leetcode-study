"""
Blind 75 - Word Break
LeetCode Problem: https://leetcode.com/problems/word-break/
시간복잡도 : O(n^2)
공간복잡도 : O(n)
풀이 : 다이나믹 프로그래밍을 이용한 풀이
문자열 s의 길이를 n이라 할 때, dp[i]를 s의 처음부터 i-1번째 문자까지의 부분 문자열이 
단어 사전에 있는 단어들로 구성될 수 있는지를 나타내는 불리언 값이라고 정의한다.
"""
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        word_set = set(wordDict)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set: # 0~j-1까지 문자열이 단어사전에 있고, j~i-1까지 문자열이 단어사전에 있는 경우
                    dp[i] = True
                    break

        return dp[len(s)]
