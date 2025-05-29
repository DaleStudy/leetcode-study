class Solution:
    """
        - Time Complexity: O(1), <= 32 bit operation
        - Space Complexity: O(1)
    """
    def getSum(self, a: int, b: int) -> int:
        # Using mask value for making 32 bit integer operation
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            xor = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK
            a, b = xor, carry
        
        # If a is overflow than MAX_INT (Negative Integer), return 2's compliment value
        return a if a <= MAX_INT else ~(a ^ MASK)

tc = [
        (1, 2, 3),
        (2, 3, 5)
]

sol = Solution()
for i, (a, b, e) in enumerate(tc, 1):
    r = sol.getSum(a, b)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
