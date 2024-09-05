"""
TC: O(n)
SC: O(n)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = list(s.lower())
        chars = []
        for c in str:
            if (ord(c) >= ord("a") and ord(c) <= ord("z")) or (ord(c) >= ord("0") and ord(c) <= ord("9")):
                chars.append(c)

        for i in range(len(chars)//2):

            if len(c)%2 == 0:
                if chars[i] != chars[-(i+1)]:
                    return False
            else:
                if chars[i] != chars[-(i+1)]:
                    return False

        return True
