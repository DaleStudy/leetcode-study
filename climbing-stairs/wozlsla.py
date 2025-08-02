"""
# Intuition
계단 정상에 오를 수 있는 방법의 수 - 1,2 - 순열? -> X. 자리수가 일정하지 않음

# Approach
접근 1) 1 or 2 로만 이동 가능

풀이 참고
- 계단을 한 번에 최대 2칸 밖에 올라갈 수 없으므로, 3번째 칸에 발을 딛기 위해서는 바로 아래 칸인 2번째 칸이나 적어도 1번째 칸에 반드시 먼저 올라와있어야 함.
- 즉, n 칸에 발을 딛기위해서는 그 전에 n - 1 칸이나 n - 2 칸까지 올라와왔어야 한다.

접근 2)
4 -> 5
1 1 1 1
2 1 1
1 2 1
1 1 2
2 2

5 -> 8
1 1 1 1 1
2 2 1
1 2 2
2 1 2
1 1 1 2
1 1 2 1
1 2 1 1
2 1 1 1

n=5까지만 봤을 때 늘어나는 규칙이 피보나치수열과 같음. (hint)

# Complexity
- Time complexity
  - DP 1 : O(N)
  - DP 2 : O(N)

  - Recursive 1 : O(2^N)
  - Recursive 2 (caching): O(N)

- Space complexity
  - DP 1 : O(N)
  - DP 2 : O(1)

  - Recursive 1 : O(N)
  - Recursive 2 (caching): O(N)

"""


# DP 2 (공간 최적화)
class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 3:
            return n

        pre, cur = 1, 2

        for _ in range(n - 2):
            pre, cur = cur, pre + cur  # 순서 !

        return cur


""" DP 1
class Solution:
    def climbStairs(self, n: int) -> int:

        dp = {1:1, 2:2}

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
"""

""" Memoization (재귀 + 캐싱)
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}   
    
        def _climb(n):
        
            if n not in memo:
                if n < 3:
                    memo[n] = n
                else:
                    memo[n] = _climb(n - 1) + _climb(n - 2)
            
            return memo[n]

        return _climb(n)
"""


""" Recursive
class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 3:
            return n

        return self.climbStairs(n-1) + self.climbStairs(n-2)
"""
