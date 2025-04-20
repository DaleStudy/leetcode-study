class Solution:
    """
        - Time Complexity: O(1)
            - n is 32bit integer
            - while loop never exceed 32 times
        - Space Complexity: O(1)
    """
    def hammingWeight(self, n: int) -> int:
        # check the most right bit, and shift right
        count = 0
        while n > 0:
            if n & 1:
                count += 1
            n >>= 1
        
        return count

tc = [
        (11, 3),
        (128, 1),
        (2147483645, 30)
]

for i, (n, e) in enumerate(tc, 1):
    sol = Solution()
    r = sol.hammingWeight(n)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
