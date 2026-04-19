class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """amount를 만들기 위해 최소한의 코인으로 구성할 수 있는 방안의 수를 구하는 함수
        동일한 동전을 여러번 사용해도 됨

        방법:
        - 방법 수를 보고 dp로 풀기로 함. 금액이 dp 단계가 됨.
            모든 금액별로, 코인 목록을 돌면서, 코인을 사용할 수 있으면 amount-coin한 금액의 방법수 + 1과 비교하기
            -> 조합이 불가능한 상태를 어떻게 판단하지? 에서 dp init을 0이 아니라 inf로 해야, 구분이 가능하다는 점.
            -> 그래서 min 비교를 현재 인덱스 dp값과 i-coin의 dp 값 + 1으로 함
            coin이 정렬되지 않은 리스트라, 정렬해, coin 값이 amount를 넘어가면 pass

        Args:
            coins (list[int]): 사용할 수 있는 동전 목록
            amount (int): 목표하는 금액

        Returns:
            int: 금액을 만들기 위해 구성할 수 있는 동전들 방안 수
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        coins.sort()
        for coin in coins:
            if coin > amount:
                continue
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != float("inf") else -1
