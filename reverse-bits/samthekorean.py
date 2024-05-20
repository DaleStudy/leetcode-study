# TC : O(1)
# SC : O(1)
# Reason : The input is fixed to be 32 bit resulting in time and space complexity being O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        binary_string = bin(n)[2:].zfill(32)
        reversed_binary_string = binary_string[::-1]

        return int(reversed_binary_string, 2)
