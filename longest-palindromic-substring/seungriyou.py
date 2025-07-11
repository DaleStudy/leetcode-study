# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome_dp(self, s: str) -> str:
        """
        [Complexity]
            - TC: O(n^2)
            - SC: O(n^2)

        [Approach]
            (1) lo == hi:       len 1짜리 substring -> True
            (2) lo + 1 == hi:   len 2짜리 substring -> s[lo] == s[hi]
            (3) 그 외:          (a) 내부 string인 s[lo + 1] ~ s[hi - 1]이 palindrome이면서,
                                (b) s[lo] == s[hi]이면 True

            => (3-a)로 인해 2D DP를 사용할 수 있으며 (dp[lo][hi] = s[lo] ~ s[hi]가 palindrome인지 여부),
            dp[lo + 1][hi - 1]을 살펴봐야 하므로 lo는 **오른쪽부터 거꾸로 순회**해야 한다. (dp[lo][..]를 채우기 위해 dp[lo + 1][..]을 봐야 함)
        """

        n = len(s)
        res_lo = res_hi = 0
        dp = [[False] * n for _ in range(n)]

        # early stop
        if n < 2 or s == s[::-1]:
            return s

        for lo in range(n - 1, -1, -1):
            for hi in range(lo, n):
                # (1) lo == hi
                if lo == hi:
                    dp[lo][hi] = True

                # (2) lo + 1 == hi
                elif lo + 1 == hi:
                    dp[lo][hi] = s[lo] == s[hi]

                # (3) otherwise (a) dp[lo + 1][hi - 1] && (b) s[lo] == s[hi]
                else:
                    dp[lo][hi] = dp[lo + 1][hi - 1] and s[lo] == s[hi]

                # update res (s[lo:hi + 1]가 palindrome이면서, 최대 길이인 경우)
                if dp[lo][hi] and res_hi - res_lo < hi - lo:
                    res_lo, res_hi = lo, hi

        return s[res_lo:res_hi + 1]

    def longestPalindrome(self, s: str) -> str:
        """
        [Complexity]
            - TC: O(n^2) (각 center에서 양쪽으로 expand)
            - SC: O(1)

        [Approach]
            palindrome은 다음의 두 케이스로 구분되므로, two-pointer로도 풀 수 있다.
            (1) substring 길이가 홀수: 가운데 원소는 확인할 필요 X
            (2) substring 길이가 짝수: 모두 확인
        """

        n, res_lo, max_len = len(s), 0, 1

        # early stop
        if n < 2 or s == s[::-1]:
            return s

        # expanding from center
        def expand(lo, hi):
            # 양쪽으로 1씩 늘려가며 가장 긴 palindrome 찾기
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            return lo + 1, hi  # s[lo + 1:hi]

        # 모든 위치에서 (1) 홀수 길이 palindrome, (2) 짝수 길이 palindrome의 max len 값 찾기
        for i in range(n - 1):
            # 홀수 길이 팰린드롬 (중심이 i)
            lo1, hi1 = expand(i, i)
            if hi1 - lo1 > max_len:
                res_lo = lo1
                max_len = hi1 - lo1

            # 짝수 길이 팰린드롬 (중심이 i, i+1)
            lo2, hi2 = expand(i, i + 1)
            if hi2 - lo2 > max_len:
                res_lo = lo2
                max_len = hi2 - lo2

        return s[res_lo:res_lo + max_len]
