class Solution:
    # Python 문자열은 immutable이라 대문자만 선택적으로 수정 불가
    # lower()를 쓰면 한번 순회하므로 가장 간단 Time O(n), Space O(n)
    def toLowerCase(self, s: str) -> str:
        return s.lower()     
