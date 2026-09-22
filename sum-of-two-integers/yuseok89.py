# TC: O(12)
# SC: O(1)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0b111111111111

        a = a & MASK
        b = b & MASK

        while b != 0:
            c = (a & b) << 1
            a = a ^ b
            b = c & MASK

        if a > (MASK >> 1):
            a = ~(a ^ MASK)

        return a

