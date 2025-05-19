# https://leetcode.com/problems/coin-change/

from functools import cache
from typing import List
import math

class Solution:
    def coinChange_n(self, coins: List[int], amount: int) -> int:
        """
        [Complexity]
            - TC: O(n * amount)
            - SC: O(n * amount)

        [Approach]
            각 coin을 무한히 많이 사용할 수 있으므로 unbounded knapsack problem 이다.
            이때, 가치를 최대화하는 것 == 동전의 개수를 최소화 하는 것이다.
            따라서 2D DP로 풀 수 있다.
        """

        INF = amount + 1
        n = len(coins)

        # dp[i][j] = i번째 coin까지 사용했을 때, j 만큼의 amount를 만들 수 있는 coin의 최소 개수
        dp = [[INF] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):  # -- coin
            dp[i][0] = 0
            for j in range(1, amount + 1):  # -- amount
                if j < coins[i - 1]:
                    dp[i][j] = dp[i - 1][j]  # 현재 coin을 넣을 수 없음
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)  # min(현재 coin을 넣지 X 경우, 현재 coin을 넣는 경우)

        return dp[n][amount] if dp[n][amount] != INF else -1

    def coinChange_1(self, coins: List[int], amount: int) -> int:
        """
        [Complexity]
            - TC: O(n * amount)
            - SC: O(amount)

        [Approach]
            매 단계에서 다음의 두 값만 확인하므로, 2D DP를 rolling array 방식으로 1D DP로 space optimize 할 수 있다.
                - dp[i - 1][j]
                - dp[i][j - coins[i - 1]]
        """

        INF = amount + 1

        dp = [INF] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for amnt in range(coin, amount + 1):
                dp[amnt] = min(dp[amnt], dp[amnt - coin] + 1)  # min(현재 coin을 넣지 X 경우, 현재 coin을 넣는 경우)

        return dp[amount] if dp[amount] != INF else -1

    def coinChange_b(self, coins: List[int], amount: int) -> int:
        """
        [Complexity]
            - TC: O(n * amount) (금액 1 ~ amount 각각에 대해 len(coins) 만큼 확인)
            - SC: O(amount) (seen & q)

        [Approach]
            BFS로 최단거리를 찾듯이 접근해도 된다. 이때의 최단거리란 최소 개수를 의미한다.
        """
        from collections import deque

        q = deque([(0, 0)])  # (총 금액, coin 개수)
        seen = {0}  # 이미 확인한 총 금액

        while q:
            amnt, n = q.popleft()

            # base condition
            if amnt == amount:
                return n

            # iter
            for coin in coins:
                if (new_amnt := amnt + coin) <= amount and new_amnt not in seen:
                    q.append((new_amnt, n + 1))
                    seen.add(new_amnt)

        return -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        [Complexity]
            - TC: O(n * amount) (금액 0 ~ amount, 각각 len(coins) 만큼 확인)
            - SC: O(amount) (@cache 저장 공간, call stack)

        [Approach]
            bottom-up이었던 DP 뿐만 아니라, 더 직관적인 top-down 접근도 가능하다.
            이때 @cache를 사용하면 memoization을 통해 더 최적화할 수 있다.
        """

        @cache
        def dp(amnt):
            # base condition
            if amnt == 0:
                return 0
            if amnt < 0:
                return math.inf

            # recur
            return min(dp(amnt - coin) + 1 for coin in coins)

        res = dp(amount)

        return res if res != math.inf else -1
