class Solution:
    def isPalindrome(self, s: str) -> bool:
        answer = ""
        for c in s:
            o = ord(c)
            if 65 <= o <=90:
                answer += chr(o+32)
            elif 97 <= o <= 122:
                answer += c
            elif 48 <= o <= 57:
                answer += c

        if answer == "" or answer == answer[::-1]:
            return True
        else:
            return False


