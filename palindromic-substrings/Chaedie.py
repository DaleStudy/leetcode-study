"""
Solution: 
    1) 자신을 기준으로 l,r 포인터로 늘려주면서 같은 문자이면 palindrome
        이를 홀수, 짝수 글자에 대해 2번 진행해주면된다.
Time: O(n^2) = O(n) * O(n/2 * 2)
Space: O(1)
    
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
                result += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
                result += 1
        return result
