"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/description/

Solution:
    This is a combinatorial problem that allows duplicates.
    We can use the formula for combinations to solve this problem.
    Let's suppose that n is the number of steps, and k is the number of 2-steps.
    Then, the number of ways to climb the stairs is n!/((n-2k)!k!).
    We can iterate through all possible values of k, and calculate the number of ways to climb the stairs.

    1. Create a dictionary to store the factorials of numbers from 0 to n.
    2. Calculate the factorials of numbers from 0 to n.
    3. Iterate through all possible values of k from 0 to n//2.


Time complexity: O(n)
Space complexity: O(n)   
"""

from collections import defaultdict


class Solution:
    def climbStairs(self, n: int) -> int:
        factorials = defaultdict(int)
        factorials[0] = 1

        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
            factorials[i] = fact

        output = 0

        for i in range(n // 2 + 1):
            num_ways = factorials[n - i] / factorials[n - (i * 2)] / factorials[i]
            output += num_ways
        return int(output)
