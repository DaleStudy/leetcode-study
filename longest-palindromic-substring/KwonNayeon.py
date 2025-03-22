"""
Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters.

Time Complexity: O(n^3)
- 모든 부분 문자열을 구할 때 O(n^2)
- 각 부분 문자열이 팰린드롬인지를 알아낼 때 O(n)

Space Complexity: O(1)

Note:
- 더 효율적인 방법 생각해보기/찾아보기
"""
# Solution 1: Brute force
# 문자열의 시작값과 끝값을 이용하여 가장 긴 팰린드롬으로 업데이트하는 방식
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        max_len = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i:j+1]

                if substr == substr[::-1]:
                    if len(substr) > max_len:
                        max_len = len(substr)
                        longest_palindrome = substr

        return longest_palindrome
