# takes n steps to reach the top
# 1 or 2 steps at a time

'''
n = 1
answer = 1

n = 2
answer = 2 
1 step + 1 step
2 step

n = 3
answer = 3
1 step + 1 step + 1 step
1 step + 2 step
2 step + 1 step

n=4
answer = 5
1 step + 1 step + 1 step + 1 step
1 step + 1 step + 2 step
1 step + 2 step + 1 step
2 step + 1 step + 1 step
2 step + 2 step

n=5
answer = 8
1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 2
1 + 1 + 2 + 1
1 + 2 + 1 + 1
1 + 2 + 2
2 + 1 + 1 + 1
2 + 1 + 2
2 + 2 + 1

1 2 3 5 8 ? ? 
'''

# 시간 복잡도 O(n)
# 공간 복잡도 O(n)
def climbStairs(self, n: int) -> int:
    dp = [0] * (n + 1)
    if n == 1:
        return 1
    elif n == 2:
        return 2
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

'''def climbStairs(self, n: int) -> int:
    if n == 1:
        return 1
    prev1, prev2 = 1, 2
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current
    return prev2
    시간 복잡도 : O(n) -> 루프가 있기에
    공간 복잡도 : O(1) -> 추가 배열 없이 상수 공간만 사용
    
    '''
    