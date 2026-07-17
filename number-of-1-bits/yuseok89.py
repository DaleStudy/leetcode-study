# TC: O(logN)
# SC: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:

        cnt = 0

        while n > 0:
            cnt = cnt + (n % 2)
            n //= 2

        return cnt

