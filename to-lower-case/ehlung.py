class Solution:
    def toLowerCase(self, s: str) -> str:
        # n = s의 길이
        # 시간 복잡도: O(n) - 각 문자를 한 번씩 확인
        # 공간 복잡도: O(n) - 변환한 문자들을 담는 리스트
        result = []
        for c in s:
            if 'A' <= c <= 'Z':
                result.append(chr(ord(c) + 32))
            else:
                result.append(c)
        return ''.join(result)
