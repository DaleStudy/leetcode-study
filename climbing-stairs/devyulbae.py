"""
Blind 75 - LeetCode Problem 70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

계단이 n개, 한 번에 1칸 또는 2칸씩 오를 수 있다.
combinations를 썼더니 시간초과 발생 (O(2^n))

DP를 이용해 시간복잡도 O(n) 공간복잡도 O(1)로 풀기
f(n) = f(n-1) + f(n-2)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        one_before = 2 # n=2
        two_before = 1 # n=1

        for _ in range(3, n+1):
            current = one_before + two_before # f(1) = f(n-1) + f(n-2)
            two_before = one_before # f 밀기
            one_before = current # f 밀기
        
        return current
    
