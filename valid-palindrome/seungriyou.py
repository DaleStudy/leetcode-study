# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)

        [Approach]
            1. non-alphanumeric 문자만 lowercase로 변환 후 리스트에 모은다.
            2. 1번의 결과를 뒤집어도 동일한지 확인한다.
        """

        s = [_s.lower() for _s in s if _s.isalnum()]

        return s == s[::-1]

    def isPalindrome1(self, s: str) -> bool:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)

        [Approach]
            1. lowercase로 변환 후 non-alphanumeric을 제거한다.
            2. 1번의 결과를 뒤집어도 동일한지 확인한다.
        """
        import re

        _s = re.sub("[^a-z0-9]", "", s.lower())

        return _s == _s[::-1]

    def isPalindrome2(self, s: str) -> bool:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)

        [Approach]
            1. lowercase로 변환 후 non-alphanumeric을 제거한다.
            2. 1번의 결과를 절반까지만 순회하며, 양끝에서부터 문자가 동일한지 확인한다.
        """
        import re

        _s = re.sub("[^a-z0-9]", "", s.lower())

        def is_palindrome(string):
            # 문자열의 절반까지만 순회하며, 양끝에서부터 문자가 동일한지 확인
            for i in range((n := len(string)) // 2):
                if string[i] != string[n - i - 1]:
                    return False
            return True

        return is_palindrome(_s)
