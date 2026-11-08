"""
 * Time Complexity: O(n)
 * Space Complexity: O(n)
"""
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = []
        for c in s:
            if 'A' <= c <= 'Z':
                # 대문자와 소문자의 차이는 5번째 비트가 0이냐 1이냐의 차이
                # 대문자인 경우 비트 OR 연산으로 5번째 비트를 1로 만든다.
                ans.append(chr(ord(c) | 32))
            else:
                ans.append(c)
        return "".join(ans)
