class Solution:
    def hammingWeight(self, n: int) -> int:
        n = int(n)
        cnt = 0
        while n > 0:
            if n % 2 == 1:
                cnt += 1
            n = n // 2
        return cnt