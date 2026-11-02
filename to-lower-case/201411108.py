class Solution:
    def toLowerCase(self, s: str) -> str:
        answer = ''

        for char in s:
            if ord(char) >= 65 and ord(char) <= 90:
                answer += chr(ord(char) + 32)
            else:
                answer += char
        
        return answer