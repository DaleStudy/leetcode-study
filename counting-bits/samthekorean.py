# TC: O(n)
# SC: O(n)
# For each number from 1 to n, update the count of set bits for i based on the count for i divided by two
# and the least significant bit (LSB) of i.
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
