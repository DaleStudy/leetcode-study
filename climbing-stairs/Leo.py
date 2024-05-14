class Solution:
    def climbStairs(self, n: int) -> int:
        fast, slow = 1, 1

        for i in range(n - 1):
            tmp = fast
            fast = fast + slow
            slow = tmp

        return fast

        ## TC: O(n), SC:O(1)
