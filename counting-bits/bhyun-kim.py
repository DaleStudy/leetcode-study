"""
338. Counting Bits
https://leetcode.com/problems/counting-bits/description/

Solution:
    - Convert the number to binary string
    - Sum the number of 1s in the binary string
    - Append the sum to the output list
    - Return the output list

Time complexity: O(nlogn)
    - The for loop runs n times
    - The sum function runs O(logn) times

Space complexity: O(n)
    - The output list has n elements
"""


from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n + 1):
            _str = str(bin(i))[2:]
            _sum = sum(map(int, _str.strip()))
            output.append(_sum)

        return output
