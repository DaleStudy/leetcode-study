class Solution:
    def reverseBits(self, n: int) -> int:
        result = []
        quotient = n
        while (quotient != 0):
            remainer = quotient % 2
            
            result.append(remainer)

            quotient = quotient // 2
        
        while len(result) < 32:
            result.append(0)  

        final_val = 0
        for bit in result:
            final_val = (final_val << 1) | bit
            
        return final_val
