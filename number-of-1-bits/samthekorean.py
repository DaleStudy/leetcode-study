# TC : O(log n)
# reason : bin method internally devides n by 2 while transitioning to binary number
# SC : O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        # count each charactor from the first
        for bit in bin(n):
            if bit == "1":
                res += 1
        return res
