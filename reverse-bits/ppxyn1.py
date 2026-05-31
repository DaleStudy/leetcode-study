# idea: -
# Time Complexity : O(1) since just fixed 32bit 

class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:]              
        bits = bits.zfill(32)          # 32bits
        reversed_bits = bits[::-1]     
        return int(reversed_bits, 2)   # binary to int 

