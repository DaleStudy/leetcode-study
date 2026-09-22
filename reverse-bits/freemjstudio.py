class Solution:
    def reverseBits(self, n: int) -> int:
        # 1. convert integer into binary
        binary = bin(n)[2:]

        # 2. convert into 32bits
        fill_zero = 32 - len(binary)
        binary = "0" * fill_zero + binary

        # 3. reverse the binary
        reversed_binary = binary[::-1]

        # 4. convert binary into integer
        return int(reversed_binary,2)
