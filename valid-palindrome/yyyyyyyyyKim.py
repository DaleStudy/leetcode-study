class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # 소문자로 변경
        s = s.lower()
        p = ""

        # 문자,숫자만 뽑기
        for i in range(len(s)):
            if (ord(s[i]) > 96 and ord(s[i]) < 123) or (ord(s[i]) >= 48 and ord(s[i]) <= 57):
                p += s[i]

        # 문자열 뒤집기
        return p == p[::-1]
