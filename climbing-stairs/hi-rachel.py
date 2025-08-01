"""
https://leetcode.com/problems/climbing-stairs/description/

한 번에 1계단 혹은 2계단 오를 수 있음
1: 1
2: 2
3: 1 + 1 + 1, 1 + 2, 2 + 1 => 3
4: 1 + 1 + 1 + 1, 1 + 1 + 2, 2 + 1 + 1, 1 + 2 + 1, 2 + 2 => 5
5: 1 + 1 + 1 + 1 + 1,
   1 + 1 + 1 + 2,
   1 + 1 + 2 + 1 + 1,
   1 + 2 + 1 + 1,
   2 + 1 + 1 + 1,
   2 + 2 + 1,
   2 + 1 + 2,
   1 + 2 + 2,
   => 8

steps[n] = steps[n - 1] + steps[n - 2]

TC: O(n)
SC: O(n)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        steps = [0] * n
        steps[0] = 1
        steps[1] = 2
        for i in range(2, n):
            steps[i] = steps[i - 2] + steps[i - 1]
        return steps[n - 1]
