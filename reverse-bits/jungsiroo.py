class Solution:
    def reverseBits(self, n: int) -> int:
        # TC : O(32)
        # SC : O(32)
        
        bit_str = ''.join(reversed(format(n, 'b').zfill(32)))
        return int(bit_str, 2)


