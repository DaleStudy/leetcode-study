# TC : O(n)
# SC : O(n)
class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFFF

        while (b & mask) > 0:

            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return (a & mask) if b > 0 else a
