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


# 7기 풀이
# 시간 복잡도: O(n)
# - memoization을 이용해 결과를 저장을 하면, 계산은 0 ~ n까지 한 번씩만 계산
# - 즉, 계단의 개수 n이 최대 계산 횟수이므로 전체 연산은 O(n)
# 공간 복잡도: O(n)
# - memoization을 하기 위한 dict에 최대 n의 개수만큼만 저장
# - 재귀 호출 스택 깊이도 최대 n
class Solution:
    # 해당 문제는 이전 계단까지 계산된 경우의 수를 찾아가며 현재 계단까지 오를 수 있는 경우의 수를 계산한다.
    # n번째 계단까지 오를 수 있는 경우의 수는 (n-1번째까지 오를 수 있는 경우의 수) + (n-2번째까지 오를 수 있는 경우의 수)이다.
    # 이는 동적 프로그래밍을 이용해 memoization을 하며 풀 수 있는 문제라고 할 수 있다.
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(n):
            # n이 0 또는 1일 경우에는 하나의 방법만 있기 때문에 memo에 1을 넣고 return해준다.
            if n <= 1:
                memo[n] = 1
                return memo[n]

            # memoization을 이미한 경우에는 memo에서 결과를 꺼내 return해준다.
            if n in memo:
                return memo[n]
            
            # (n번째까지 오를 수 있는 경우의 수) = (n-1번째까지 오를 수 있는 경우의 수) + (n-2번째까지 오를 수 있는 경우의 수)
            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]

        return dfs(n)
