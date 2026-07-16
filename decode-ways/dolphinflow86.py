# 1) Top-down DP (Recursion + Memoization)
# At each step, recurse down one and two digit case. Memoization is required due to overlapping subproblems.
# TC: O(N) where N is the length of the string
# SC: O(N) where N is the length of the string (recursion stack space and memo array)
class Solution:
    def decode(self, s: str, idx: int, memo: List[int]) -> int:
        if idx == len(s): return 1
        if idx > len(s): return 0
        if int(s[idx]) == 0: return 0

        if memo[idx] != -1: return memo[idx]

        # 1 digit
        ways = self.decode(s, idx + 1, memo)
        
        # 2 digits
        if idx + 2 <= len(s):
            num = int(s[idx:idx+2])
            if 10 <= num <= 26:
                ways += self.decode(s, idx + 2, memo)

        memo[idx] = ways
        return ways

    def numDecodings(self, s: str) -> int:
        # 11106
        memo = [-1] * len(s)
        return self.decode(s, 0, memo)
