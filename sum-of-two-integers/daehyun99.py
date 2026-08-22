# Time: O(1)
# Space: O(1)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0 :
            carry = (a&b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)

"""
# Time: O(N)
# Space: O(N)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        pos = []
        neg = []

        for i in [a, b]:
            if i < 0 :
                for j in range(i, 0):
                    neg.append(0)
            else:
                for j in range(i):
                    pos.append(0)
        if len(neg) <= len(pos):
            for i in range(len(neg)):
                pos.pop()
            return len(pos)
        else:
            for i in range(len(pos)):
                neg.pop()
            return -1 * len(neg)
"""
