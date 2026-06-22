class Solution:
    """
    풀이 1: 투포인터
    TC: O(n)
    SC: O(1)

    양쪽 끝에서 포인터를 좁혀가며 알파벳/숫자만 비교.
    """
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    """
    풀이 2: 리스트 변환 + 역순 비교
    TC: O(n)
    SC: O(n)

    알파벳/숫자만 추출한 리스트를 역순과 비교.
    """
    def isPalindrome2(self, s: str) -> bool:
        s = [c for c in s.lower() if c.isalnum()]
        return s == s[::-1]
