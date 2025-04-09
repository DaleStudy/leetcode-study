"""
계단 오르기
맨 꼭대기 가는데 n steps만큼 걸림

매번 올라가는데 1 or 2 계단 오르기 가능!

Inputs: n

Outputs: how many distinct ways to get to the top?

Constraints: 1 <= n <= 45

Time Complexity: O(2^n)

계단 오르는 방법 중, 중복되지 않는 모든 가지 수 구하기
우선 완탐으로 해보고, 그 다음 최적부분구조 할 수 있는지 체크

n = 2

1 1 -> dp[1]
2 0 -> dp

2     dp(n - 2) + dp(n - 1) + 1

n = 3
2 1
1 1 1 => dp[2] 값

1 2 => 여기선 dp[2] 로 가면 안됨!

1 2
1 1 1 => dp[2] 값

2 1 => 이건 dp[1] 값


n = 4
1 3 => dp[3]
2 2 => dp[2]

n = 5
2 2 1
2 1 2
1 2 2

n = 6

5 1
4 2

n = 7

6 1
5 4
4 3

특정 수를 구성하는 1과 2의 배열 가짓수들이 정해져있음!!

한 호출마다 뻗어지는 가짓수, 즉 호출수를 모르겠어서 시간복잡도 모르겠음

점화식을 어떻게 세우지?

3
1 2

기저조건또 헷갈...   n 3 // 2 + 1

하지만, 도식화해보니
결국 dp(n) = dp(n - 1) + dp(n - 2)

1 2
1 1 1 => dp[2] 값

2 1 => 이건 dp[1] 값

Space Complexity: O(n)
dp 배열 n만큼의 크기 지님

"""


class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        def climb(n):

            if dp[n]:
                return dp[n]

            else:
                dp[n] += climb(n - 1) + climb(n - 2)
                return dp[n]

        return climb(n)

# sol = Solution()
# sol.climbStairs(3)
