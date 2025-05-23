# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings_dp(self, s: str) -> int:
        """
        [Complexity]
            - TC: O(n^2)
            - SC: O(n^2)

        [Approach]
            palindromic substring인지 여부를 확인하기 위해, 크게 두 가지 경우에 대해 고려해야 한다.
                - 길이가 홀수: len == 1인 단위 substring에서 좌우로 확장
                - 길이가 짝수: len == 2인 단위 substring에서 좌우로 확장

            이때, 기존의 짧은 substring에서 판단한 결과를 계속해서 재사용하므로 다음의 DP table을 사용하는 2D DP로 풀 수 있다.
                dp[i][j] = s[i:j + 1]이 palindromic substring인지 여부

            따라서 다음과 같이 1) & 2)에서 길이가 각각 1, 2인 단위 substring에 대해 초기화를 먼저 수행하고, 3)에서 len >= 3이상인 substring에 대해 판단한다.
            단, **더 짧은 안 쪽 substring에서의 판단 결과를 사용해야 하므로** len을 3부터 n까지 늘려가면서, two pointer i & j로 판단한다.
                1) length = 1   : dp[i][i]은 무조건 True
                2) length = 2   : dp[i][i + 1]은 s[i] == s[i + 1]이면 True
                3) length >= 3  : (j = i + length - 1일 때) dp[i][j]은 (s[i] == s[j]) && (dp[i + 1][j - 1])이면 True
        """

        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = 0

        # 1) length = 1   : dp[i][i]은 무조건 True
        for i in range(n):
            dp[i][i] = True
            res += 1

        # 2) length = 2   : dp[i][i + 1]은 s[i] == s[i + 1]이면 True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                res += 1

        # 3) length >= 3  : (j = i + length - 1일 때) dp[i][j]은 s[i] == s[j]이면서 dp[i][j - 1]이면 True
        for length in range(3, n + 1):  # length는 3부터 n까지 늘려나가기 (**더 짧은 substring에서의 판단 결과를 사용해야 하므로**)
            for i in range(n - length + 1):  # i = substring 시작 인덱스
                j = i + length - 1  # j = substring 종료 인덱스
                if s[i] == s[j] and dp[i + 1][
                    j - 1]:  # (1) i & j가 가리키는 문자가 서로 같고 (2) 안 쪽 substring이 palindrome 이라면 palindromic substring
                    dp[i][j] = True
                    res += 1

        return res

    def countSubstrings_dp2(self, s: str) -> int:
        """
        [Complexity]
            - TC: O(n^2)
            - SC: O(n^2)

        [Approach]
            length <= 2 조건을 or 연산으로 연결함으로써 1), 2), 3) 케이스를 하나로 줄일 수 있다.
        """

        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = 0

        for length in range(1, n + 1):  # length는 1부터 n까지 늘려나가기 (**더 짧은 substring에서의 판단 결과를 사용해야 하므로**)
            for i in range(n - length + 1):  # i = substring 시작 인덱스
                j = i + length - 1  # j = substring 종료 인덱스
                if s[i] == s[j] and (length <= 2 or dp[i + 1][j - 1]):  # length <= 2 조건을 or 연산으로 연결
                    dp[i][j] = True
                    res += 1

        return res

    def countSubstrings(self, s: str) -> int:
        """
        [Complexity]
            - TC: O(n^2)
            - SC: O(1)

        [Approach]
            palindromic substring인지 여부를 확인하기 위해, 크게 두 가지 경우에 대해 고려해야 한다.
                - 길이가 홀수: len == 1인 단위 substring에서 좌우로 확장
                - 길이가 짝수: len == 2인 단위 substring에서 좌우로 확장

            따라서 s를 순회하며, 각 문자를 center로 하여 만들 수 있는 길이가 홀수 & 짝수인 palindrome의 개수를 좌우로 확장해가며 카운트한다.
        """

        def count_palindrome_from_center(lo, hi):
            cnt = 0

            # lo와 hi가 범위를 벗어나지 않도록
            while (lo >= 0 and hi < len(s)):
                # lo와 hi가 가리키는 문자가 다르다면 더이상 확장하며 palindrome을 찾을 수 없음
                if s[lo] != s[hi]:
                    break

                # lo와 hi를 좌우로 확장
                lo -= 1
                hi += 1

                # palindrome 개수 증가
                cnt += 1

            return cnt

        res = 0

        # center 인덱스 순회
        for i in range(len(s)):
            # 길이가 홀수: len == 1인 단위 substring에서 좌우로 확장
            res += count_palindrome_from_center(i, i)

            # 길이가 짝수: len == 2인 단위 substring에서 좌우로 확장
            res += count_palindrome_from_center(i, i + 1)

        return res
