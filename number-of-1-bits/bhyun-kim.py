"""
191. Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/

Solution:
    - Create a counter
    - For each bit in the input number:
        - If the bit is 1:
            - Increment the counter
    - Return the counter

Time complexity: O(1)
    - The while loop runs 32 times

Space complexity: O(1)
    - No extra space is used
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0

        i = 1 << 31
        while i > 0:
            if (n & i) != 0:
                output += 1

            i = i >> 1

        return output
