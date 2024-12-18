class Solution(object):
    def climbStairs(self, n):
        
        import math

        # Second method - n = 2x+y
        if n % 2 == 0:
            max = n //2
        else:
            max = (n-1) // 2
        
        total_methods = 0

        for i in range(0, max+1):
            y = n - (2 * i)
            total_steps = i + y

            total_permu = math.factorial(total_steps) // (math.factorial(i) * math.factorial(y))
            total_methods += total_permu

        return total_methods
    

    # First attempt to this question. 
    # Get dividend and remainder of 2 steps & get all combinations & add one additional method for all 1 step combination
    # But how to get all combinations? => permutation
    # def climbStairs(self, n):
    #     # 2 steps
    #     two_steps = n // 2
    #     two_steps_remainder = n % 2

    #     total_steps = two_steps + two_steps_remainder
        
    #     total_permu = math.factorial(total_steps) // (math.factorial(two_steps) * math.factorial(two_steps_remainder))
    #     total_permu += 1

    #     return total_permu