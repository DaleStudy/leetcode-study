# 문제: https://neetcode.io/problems/string-encode-and-decode
# TC: O(N), SC: O(1)
# ASCII 문자열이 아닌 이모티콘으로 구분자 선택

class Solution:
    def encode(self, strs: List[str]) -> str:
        return '🤍'.join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split('🤍')

# ASCII 문자열에 포함된 기호로 구분자를 써야할 때
# -> 글자 수 표시
class Solution:
    def encode(self, strs: List[str]) -> str:
        text = ""
        for str in strs:
            text += f"{len(str)}:{str}"
        return text

    def decode(self, s: str) -> List[str]:
        ls, start = [], 0
        while start < len(s):
            mid = s.find(":", start)
            length = int(s[start : mid])
            word = s[mid + 1 : mid + 1 + length]            
            ls.append(word)
            start = mid + 1 + length
        return ls
    
