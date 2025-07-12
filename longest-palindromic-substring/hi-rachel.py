"""
https://leetcode.com/problems/longest-palindromic-substring/

문자열 s가 주어졌을 때, 가장 긴 팰린드롬 부분 문자열을 찾아서 반환하는 함수를 작성해라.

문제 풀이

1. 문자열 `s`의 모든 인덱스 `i`를 기준으로,
2. 두 종류의 중심에서 팰린드롬을 확장해 본다:
   - 홀수 길이: `s[i]`를 중심으로 좌우 확장 (`i, i`)
   - 짝수 길이: `s[i]`와 `s[i+1]`을 중심으로 좌우 확장 (`i, i+1`)
3. 각 중심에서 while문으로 `s[left] == s[right]`인 동안 확장
4. 가장 긴 팰린드롬 문자열을 계속 업데이트
5. 최종적으로 가장 긴 팰린드롬을 반환한다

TC: O(n^2)
SC: O(1)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                
            return s[left + 1 : right]

        res = ""
        for i in range(len(s)):
            temp1 = expand(i, i)    # 홀수 길이 팰린드롬
            temp2 = expand(i, i+1)  # 짝수 길이 팰린드롬
            if len(temp1) > len(res):
                res = temp1
            if len(temp2) > len(res):
                res = temp2
        return res
