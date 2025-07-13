"""
Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters.

<Solution 1: Brute force>
- 문자열의 시작값과 끝값을 이용하여 가장 긴 팰린드롬으로 업데이트하는 방식

Time Complexity: O(n^3)
- 모든 부분 문자열을 구할 때 O(n^2)
- 각 부분 문자열이 팰린드롬인지를 알아낼 때 O(n)

Space Complexity: O(1)
"""
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

"""
<Solution 2: 투 포인터 방법>
- 투 포인터를 활용하여 중심에서부터 팰린드롬 여부 체크

Time Complexity: O(n^2)
- 메인 루프: O(n) - 각 위치 i에 대해 반복
- 각 루프에서 expandAroundCenter 호출: 최악의 경우 O(n) - 전체 문자열까지 확장 가능

Space Complexity: O(1)
- 추가 변수를 사용하지 않음
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0
        max_len = 1

        for i in range(len(s)):

            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)

            current_max = max(len1, len2)

            if current_max > max_len:
                max_len = current_max
                start = i - (current_max - 1) // 2

        return s[start:start + max_len]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1
