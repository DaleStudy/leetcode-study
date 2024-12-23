"""
dp 문제는 아직 어색해서 직접 풀진 못했습니다.
"""

"""
재귀와 dp hash_map 을 활용한 캐싱 전략
Time: O(n)
Space: O(n) = O(n) + O(n)
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            # 한자리 숫자
            res = dfs(i + 1)

            # 두자리 숫자
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)


"""
iterative dp
Time: O(n)
Space: O(n)
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]
