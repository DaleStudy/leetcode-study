class Solution:
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        """
        - Idea: 아래의 방법으로 주어진 문자열에서 가장 긴 팰린드롬을 찾는다.
            1. 모든 가능한 부분 문자열 생성
            2. 각 부분 문자열이 팰린드롬인지 확인
            3. 가장 긴 팰린드롬을 저장하고 반환
        - Time Complexity: O(n^3). n은 문자열의 길이
            모든 부분 문자열을 구하는데 O(n^2), 각 부분 문자열이 팰린드롬인지 알아내는데 O(n).
            결국 O(n^3)의 시간이 소요된다.
        - Space Complexity: O(n). n은 문자열의 길이
            팰린드롬인지 확인할 때 문자열 슬라이싱을 사용하는데,
            최악의 경우 부분 문자열의 길이가 입력 문자열의 길이와 같아
            공간 복잡도는 O(n)이다.
        """

        result = s[0]

        for i in range(len(s) - 1):
            for j in range(i + 1, len(s) + 1):
                if j - i <= len(result):
                    continue

                if self.is_palindrome(s[i:j]) and (j - i) > len(result):
                    result = s[i:j]

        return result
