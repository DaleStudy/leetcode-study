class Solution:
    # n번째 계단에 오를 수 있는 방법 수는 (n - 1번째 계단에 오르는 방법 수) + (n - 2번째 계단에 오르는 방법 수)와 같다.
    # 이는 피보나치 수열 공식에 기반하며, 피보나치 수열 상 n번째 오는 수가 곧 답이 된다.
    def climbStairs(self, n: int) -> int:
        memo = [1, 1, 2]

        def fibonacci(step):
            if step > n:
                return

            ways = memo[step - 1] + memo[step - 2]
            memo.append(ways)
            fibonacci(step + 1)

        fibonacci(3)

        return memo[n]
