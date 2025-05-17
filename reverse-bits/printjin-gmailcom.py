class Solution:
    def reverseBits(self, n):
        b = bin(n)[2:]              
        b = b.zfill(32)             
        reversed_b = b[::-1]        
        return int(reversed_b, 2) 
