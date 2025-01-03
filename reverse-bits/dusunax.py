'''
# 190. Reverse Bits

SolutionA: using bin() and int() to convert the types.
SolutionB: using bitwise operations to reverse the bits.

## Time and Space Complexity

### SolutionA
```
TC: O(32) -> O(1)
SC: O(1)
```

### SolutionB
```
TC: O(32) -> O(1)
SC: O(1)
```
'''
class Solution:
    '''
    SolutionA
    - using bin() and int() to convert the number to binary and back to integer.
    - use .zfill(32) ensures that the binary string is always 32 bits long.
    '''
    def reverseBitsA(self, n: int) -> int:
        bit = bin(n)[2:].zfill(32)
        return int(bit[::-1], 2)
  
    '''
    SolutionB
    - using bitwise operations to reverse the bits.
    - iterate through the bits and reverse them.
    '''
    def reverseBitsB(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1) # shift the result to the left & add LSB of n
            n >>= 1 # shift n to the right & remove previous LSB
        return result
