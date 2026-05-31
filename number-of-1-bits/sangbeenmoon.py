class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            if n % 2 == 1:
                cnt = cnt + 1
            n = n // 2
            print(n)
        return cnt
