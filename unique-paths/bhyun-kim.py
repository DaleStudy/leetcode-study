"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/

Solution:
    To solve this problem, we can use the combinatorics approach.
    We can calculate the number of unique paths using the formula C(m+n-2, m-1).
    We can create a helper function to calculate the factorial of a number.
    We calculate the numerator and denominator separately and return the result.

Time complexity: O(m+n)
    - We calculate the factorial of m+n-2, m-1, and n-1.
    - The time complexity is O(m+n) for calculating the factorials.

Space complexity: O(1)
    - We use a constant amount of extra space.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(num):
            previous = 1
            current = 1
            for i in range(2, num + 1):
                current = previous * i
                previous = current
            return current

        max_num = m + n - 2
        numerator = factorial(max_num)
        factorial_m_minus_1 = factorial(m - 1)
        factorial_n_minus_1 = factorial(n - 1)
        result = numerator // (factorial_m_minus_1 * factorial_n_minus_1)
        return result
