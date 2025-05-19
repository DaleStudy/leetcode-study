class Solution:
    """
        - Time Complexity: O(1), 32 times calculation
        - Space Complexity: O(1)
    """
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1

        return result

tc = [
        (43261596, 964176192),
        (4294967293, 3221225471)
]

sol = Solution()
for i, (n, e) in enumerate(tc, 1):
    r = sol.reverseBits(n)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
