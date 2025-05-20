# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits_32(self, n: int) -> int:
        """
        [Complexity]
            - TC: O(32)
            - SC: O(1)

        [Approach]
            n의 맨 오른쪽 bit부터 res의 맨 왼쪽에 붙여나가기
        """
        res = 0
        for i in range(32):
            res |= ((n >> i) & 1) << (31 - i)
        return res

    def reverseBits(self, n: int) -> int:
        """
        [Complexity]
            - TC: O(16)
            - SC: O(1)

        [Approach]
            n의 바깥쪽에서부터 two pointer 처럼 res에 모으기
        """
        res = 0
        for i in range(16):
            left = (n >> (31 - i)) & 1
            right = (n >> i) & 1
            res |= (left << i) | (right << (31 - i))
        return res
