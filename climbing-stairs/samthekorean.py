# TC: O(n) — the loop runs n-2 times in the worst case
# SC: O(1) — only a constant number of variables are used (a, b, c)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 :
            return 1
        if n == 2 :
            return 2

        a = 1
        b = 2

        for i in range(n - 2) :
            c = a + b
            a = b
            b = c

        return b 
        
            
# 이전 풀이
# Time complexity : O(n)
# Space complexity : O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        result = 0
        if n == 1:
            return a

        if n == 2:
            return b

        for i in range(3, n + 1):
            result = a + b
            a, b = b, result

        return result
    
