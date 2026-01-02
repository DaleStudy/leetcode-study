"""
Blind75 - Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/
시간복잡도 : O(log n)
공간복잡도 : O(1)

풀이 :
    파이썬의 내장함수 bin() -> O(log n)
    문자열 메서드 count() -> O(log n)

"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')
    

