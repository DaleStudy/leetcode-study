class Solution:
    def reverseBits(self, n: int) -> int:
        digits = bin(n)[2:]
        digits = list(digits)[::-1]

        while len(digits) < 32:
            digits.append("0")
        
        return int("".join(digits), 2)
