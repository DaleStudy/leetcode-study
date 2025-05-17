"""
[문제풀이]
# Inputs
- 정수 배열 coins
- 총 돈의 값 amount
# Outputs
- amount 를 채울 수 있는 동전의 가장 적은 수
- 만약 만들 수 없다면 -1 return
# Constraints
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
# Ideas
- 우선 이전 풀이 본 거 연습해보기
- DP 탑다운 방식으로! 이 문제 풀이를 내가 100% 이해하고 있는게 맞는지 손으로 도식화 해보기로함


[회고]
재귀랑 dp는 다양한 유형을 많이 풀어보는 수 밖에..
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amount):

            if amount == 0:
                return 0

            retList = []
            for coin in coins:
                if amount - coin >= 0:
                    if amount - coin not in memo:
                        memo[amount - coin] = dp(amount - coin)

                    if memo[amount - coin] != -1:
                        retList.append(memo[amount - coin])

            return min(retList) + 1 if retList else -1

        return dp(amount)


