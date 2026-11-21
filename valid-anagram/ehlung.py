"""
n = s의 길이
시간 복잡도: O(n) - s와 t를 한 번씩 돌면서 확인 (딕셔너리 조회/수정은 O(1))
공간 복잡도: O(1) - 소문자만 나와서 딕셔너리 키가 최대 26개
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        for ch in s:
            if ch in s_count:
                s_count[ch] += 1
            else:
                s_count[ch] = 1

        for ch in t:
            # ch가 없는 경우를 먼저 검사해야 뒤에서 KeyError가 안 남
            if ch not in s_count or s_count[ch] == 0:
                return False
            # 여기서 return하면 함수가 끝나니까 뒤에 else 안붙어도 됨
            s_count[ch] -= 1

        return True
