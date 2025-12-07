class Solution:
    def climbStairs(self, n: int) -> int:
        if (n<1 or n>45):
            return 0
        
        def factorial(num):
            if num <= 1:
                return 1
            
            result = 1 
            for i in range(2, num+1):
                result *= i
            return result 

        steps = 0
        cur_steps = 1
        quotient = n // 2
        k=0
       
        for _ in range(quotient+1):  
            cur_steps = factorial(n-k) / (factorial(k)*factorial(n-2*k))  
            k+=1
            steps += cur_steps

        return int(steps)


