# 1) Divide by 2 and count set bit.
# TC: O(logN) where N is the given number.
# SC: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        setbit_count = 1

        while n >= 2:
           if n % 2 == 1: setbit_count += 1
           n = n // 2
        return setbit_count
