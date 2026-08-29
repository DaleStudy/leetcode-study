# TC: O(N)
# SC: O(N)
class Solution:

    memo = []

    def rec(self, idx, s, n):
        if self.memo[idx] == -1:

            cnt = 0

            if int(s[idx]) != 0:
                cnt += self.rec(idx + 1, s, n)

            if idx + 1 < n:
                if int(s[idx]) != 0 and int(s[idx]) * 10 + int(s[idx + 1]) <= 26:
                    cnt += self.rec(idx + 2, s, n)

            self.memo[idx] = cnt

        return self.memo[idx]

    def numDecodings(self, s: str) -> int:

        self.memo = [-1] * (len(s) + 1)
        self.memo[len(s)] = 1

        return self.rec(0, s, len(s))

