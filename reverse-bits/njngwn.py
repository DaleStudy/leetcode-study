class Solution:
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def reverseBits(self, n: int) -> int:
        stack = []
        for i in range(32):
            stack.append(n % 2)
            n //= 2

        res, multiples = 0, 1
        while stack:
            res += (stack.pop() * multiples)
            multiples *= 2

        return res
