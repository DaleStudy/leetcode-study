class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Climbing Stairs Problem: You are climbing a staircase with n steps.
        Each time you can either climb 1 or 2 steps. How many distinct ways can you climb to the top?

        This is essentially a Fibonacci sequence problem:
        - To reach step n, you can either:
          1. Take a single step from step (n-1)
          2. Take a double step from step (n-2)
        - Therefore, the total ways to reach step n = ways to reach (n-1) + ways to reach (n-2)

        Time Complexity: O(n) - We need to calculate each step once
        Space Complexity: O(1) - We only store two previous values regardless of input size
        """
        # Base cases: There's only 1 way to climb 1 step and 2 ways to climb 2 steps
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize variables with base cases
        # For staircase with 1 step, there's only 1 way to climb
        ways_to_reach_n_minus_2 = 1

        # For staircase with 2 steps, there are 2 ways to climb (1+1 or 2)
        ways_to_reach_n_minus_1 = 2

        # Variable to store the current calculation
        ways_to_reach_current_step = 0

        # Start calculating from step 3 up to step n
        for _ in range(3, n + 1):
            # To reach current step, we can either:
            # 1. Take a single step after reaching step (n-1)
            # 2. Take a double step after reaching step (n-2)
            # So the total ways = ways to reach (n-1) + ways to reach (n-2)
            ways_to_reach_current_step = (
                ways_to_reach_n_minus_1 + ways_to_reach_n_minus_2
            )

            # Shift our window of calculations forward:
            # The previous (n-1) step now becomes the (n-2) step for the next iteration
            ways_to_reach_n_minus_2 = ways_to_reach_n_minus_1

            # The current step calculation becomes the (n-1) step for the next iteration
            ways_to_reach_n_minus_1 = ways_to_reach_current_step

        # After the final iteration, both ways_to_reach_n_minus_1 and ways_to_reach_current_step
        # have the same value (the answer for step n)
        return ways_to_reach_n_minus_1  # Could also return ways_to_reach_current_step
