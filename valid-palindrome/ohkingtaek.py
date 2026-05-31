class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        - 시간복잡도: O(n)
        - 공간복잡도: O(n)
        1. 문자열을 소문자로 변환하고, 알파벳과 숫자만 남기기
        2. 남은 문자열을 절반으로 나누고, 앞과 뒤를 비교하여 회문인지 확인
        3. 회문이면 True, 아니면 False 반환
        """
        a = ""
        for i in s.lower():
            if i.isalnum():
                a += i
        for i, j in zip(a[:len(a) // 2], a[len(a):(len(a) // 2 - 1):-1]):
            if i != j:
                return False
        return True
