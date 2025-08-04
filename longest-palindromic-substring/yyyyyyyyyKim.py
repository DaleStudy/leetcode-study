"""
LeetCode 5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

summary:
주어진 문자열 s에서 "가장 긴 팰린드룸 부분 문자열"을 찾아 반환
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # DP (시간복잡도 O(n^2), 공간복잡도 O(n^2))
        n = len(s)
        dp = [[False]*n for _ in range(n)]  # dp[i][j] = s[i..j]의 팰린드룸 여부 저장
        answer = ''

        # i = 부분 문자열의 길이(1부터 n까지)
        for i in range(1,n+1):
            # j = 부분 문자열의 시작 인덱스
            for j in range(n - i + 1):
                # 끝 인덱스 = 시작인덱스 + 길이 - 1
                end = j + i -1
                # 양 끝 문자가 같을 경우
                if s[j] == s[end]:
                    # 길이가 3이하면 팰린드룸
                    if i <= 3:
                        dp[j][end] = True
                    # 양 끝이 같고 안쪽도 팰린드룸이면 전체도 팰린드룸
                    else:
                        dp[j][end] = dp[j+1][end-1]
                    
                    # 현재 팰린드룸의 길이가 answer보다 길면 업데이트
                    if dp[j][end] and i > len(answer):
                        answer = s[j:end+1]
        
        return answer
