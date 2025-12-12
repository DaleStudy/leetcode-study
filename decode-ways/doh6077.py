class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        cur = 1
        pre1 = pre2 = 1
        for i in range(2, n+1):
            one = int(s[i-1])
            two = int(s[i-2:i])
            cur = 0
            if 1 <= one <= 9:
                cur += pre1
            if 10 <= two <= 26:
                cur += pre2

            pre2 = pre1
            pre1 = cur

        return cur
