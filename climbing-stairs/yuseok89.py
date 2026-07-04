# TC: O(N)
# SC: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:

        one_down = 1
        two_down = 0

        for _ in range(1, n):
            cur = two_down + one_down
            two_down = one_down
            one_down = cur

        return two_down + one_down

