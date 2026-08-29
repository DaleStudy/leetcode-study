# TC: O(K)
# SC: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for _ in range(32):
            ans *= 2
            ans += n % 2
            n //= 2

        return ans

