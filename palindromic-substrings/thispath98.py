class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Intuition:
            2중 루프를 돌면서 각 substring에 대해
            palindrome인지 아닌지 확인한다.
            한번 palindrome인지 확인했으면, set에 추가하여
            중복 확인을 한다.

        Time Complexity:
            O(N^2 x s.length):
                2중 루프는 N^2만큼 소요되고,
                각 루프에 palindrome을 체크하는 것은
                s.length만큼 소요된다.

        Space Complexity:
            O(N^2):
                palindrome이 모두 중복되지 않을 경우 set에
                s의 substring 개수만큼 저장한다.
                이는 대략 N^2이다.
        """
        def is_palindrome(s):
            return s == s[::-1]

        palindrome_set = set()
        answer = 0
        for i in range(1, len(s) + 1):
            for j in range(0, len(s) - i + 1):
                substr = s[j: j + i]
                if substr in palindrome_set or is_palindrome(substr):
                    palindrome_set.add(substr)
                    answer += 1
        return answer
