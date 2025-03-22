"""
Solution: 
    1) 포문을 돌면서 좌우 투포인터로 벌려주며 같은 문자인지 확인한다. 같으면 팰린드롬, 아니면 break
    2) 홀수, 짝수를 별도로 순회한다.

Time: O(n^2)
Space: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]

        for i in range(len(s)):
            # check odd
            word = s[i]
            left, right = i - 1, i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    word = s[left] + word + s[right]
                    if len(result) < len(word):
                        result = word
                    left -= 1
                    right += 1
                else: 
                    break

            word = ""
            left, right = i, i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    word = s[left] + word + s[right]
                    if len(result) < len(word):
                        result = word
                    left -= 1
                    right += 1
                else: 
                    break

        return result
