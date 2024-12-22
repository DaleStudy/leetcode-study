'''
solution: 
    # dp[1] = 1step = 1
    # dp[2] = (1step + 1step) + 2step = 2
    # dp[3] = (dp[3 - 1] + 1step) + dp[3 - 2] + 2step = 2 + 1 = 3
    # dp[4] = (dp[4 - 1] + 1step) + (dp[4 - 2] + 2tep) = 3 + 2 = 5

    # dp[n] = (dp[n-1] + 1) + (dp[n-2] + 1)

time O(n)
space O(n)

'''

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]
        dp.append(1)
        dp.append(2)
        
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]

'''
solution2:
    위 솔루션에서 공간 복잡도 최적화

time O(n)
space O(1)
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        pt1, pt2 = 1,1
        for i in range(2, n+1):
            temp = pt2
            pt2 = pt1 + pt2
            pt1 = temp
        return pt2