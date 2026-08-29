class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = ""

        s = s.lower()

        for string in s:
            if 97 <= ord(string) <= 122 or 48 <= ord(string) <= 57:
                forward += string
        backward = forward[::-1]

        return True if forward == backward else False
