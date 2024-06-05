"""
338. Counting Bits
https://leetcode.com/problems/counting-bits/description/

Solution 1:
    - Convert the number to binary string
    - Sum the number of 1s in the binary string
    - Append the sum to the output list
    - Return the output list

Time complexity: O(nlogn)
    - The for loop runs n times
    - The sum function runs O(logn) times

Space complexity: O(n)
    - The output list has n elements
    
class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n + 1):
            _str = str(bin(i))[2:]
            _sum = sum(map(int, _str.strip()))
            output.append(_sum)

        return output
"""

"""
Solution 2
    We can solve this problem with dynamic programming. 
    1. Initialize output with n elements 
    2. The first element is 0 because iteration starts from zero. 
    3. Iterate from 1 to n+1 
    4. The last digit of each number is 0 for even number 1 for odd number 
        So add (i & 1) to the output 
    5. The digits except the last one can be found when the number is divided by two. 
        Instead for division by two, we can use one step of bit shift to the right. 

    0 = 00000
    1 = 00001
    2 = 00010
    3 = 00011
    4 = 00100
    5 = 00101
    6 = 00110
    7 = 00111

Time complexity: O(n)
    - The for loop runs n times

Space complexity: O(n)
    - The output list has n elements
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)

        for i in range(1, n + 1):
            output[i] = output[i >> 1] + (i & 1)

        return output
