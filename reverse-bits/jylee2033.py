class Solution:
    def reverseBits(self, n: int) -> int:
        # 0100

        res = 0

        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1

        return res

# Time Complexity: O(1)
# Space Complexity: O(1)
