"""
190. Reverse Bits
https://leetcode.com/problems/reverse-bits/description/

Solution:
    - Convert the number to binary string
    - Reverse the binary string
    - Convert the reversed binary string to integer
    - Return the integer

Time complexity: O(1)
    - The bin function runs once
    - The reversed function runs once
    - The int function runs once

Space complexity: O(1)
    - No extra space is used

"""


class Solution:
    def reverseBits(self, n: int) -> int:
        n_bin = bin(n)[2:].zfill(32)
        n_bin = "".join(reversed(n_bin))
        return int(n_bin, base=2)
