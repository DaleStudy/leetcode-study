# TC : O(n)
# SC : O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        # count each charactor from the first
        for bit in bin(n):
            if bit == "1":
                res += 1
        return res
