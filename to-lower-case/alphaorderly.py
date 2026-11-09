"""
시간 복잡도 : O(n)
공간 복잡도 : O(n)
"""
class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join((chr(ord(ch) + 32) if 65 <= ord(ch) <= 90 else ch) for ch in s)
