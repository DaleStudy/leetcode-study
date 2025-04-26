# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight1(self, n: int) -> int:
        """
        [Complexity]
            - TC: O(logn) (어차피 O(1))
            - SC: O(1)

        [Approach]
            Bit manipulation을 이용하여 n이 0이 될 때까지 다음을 반복한다.
                1) 맨 오른쪽의 bit가 1이면 res에 1을 더하고, 0이면 0을 더한다.
                2) n을 오른쪽으로 1 shift 한다.
        """
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

    def hammingWeight2(self, n: int) -> int:
        """
        [Complexity]
            - TC: O(k) (k = number of set bits)
            - SC: O(1)

        [Approach] Brian Kernighan's Algorithm
            오른쪽에서부터 1인 bit를 하나씩 지워가며 개수를 세면 된다.
            이때, 오른쪽에서부터 1인 bit를 지우기 위해서는 n & n - 1 을 하면 된다.
            (ref: https://leetcode.com/problems/number-of-1-bits/solutions/4341511/faster-lesser-3-methods-simple-count-brian-kernighan-s-algorithm-bit-manipulation-explained)
        """
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

    def hammingWeight(self, n: int) -> int:
        """
        [Complexity]
            - TC: O(logn) (어차피 O(1))
            - SC: O(1)

        [Approach]
            n을 2로 나누면서 그 나머지 값이 1이면 res에 1을 더하고, 0이면 0을 더한다.
        """
        res = 0
        while n:
            d, m = divmod(n, 2)
            res += m
            n = d
        return res
