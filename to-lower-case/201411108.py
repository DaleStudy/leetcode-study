# TC: O(n)
# SC: O(n)
class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []

        for char in s:
            if 'A' <= char <= 'Z':
                result.append(chr(ord(char) + ord('a') - ord('A')))
            else:
                result.append(char)
        
        return ''.join(result)
