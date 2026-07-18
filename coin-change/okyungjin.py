# coins: 동전의 가격이 적힌 정수 배열, 각 숫자는 유니크함, 정렬에 대한 언급 X, (1 <= coins.length <= 12)
# amount: 돈의 총합

# amount를 만들 수 있는 가장 적은 동전의 수를 반환한다.
# coins로 amount를 만들 수 없는 경우 -1을 반환
# 동전의 종류는 무한대라고 가정하고 문제를 풀 것

# 처음에는 greedy로 접근하려고 했는데, 금액이 큰 동전을 먼저 선택하는게 최소 동전의 수가 아니라서 dp로 풀이했다.

# [복잡도]
# C: 코인의 개수, # A: amount
# 시간 복잡도: O(A * C)
# 공간 복잡도: O(A)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        NOT_POSSIBLE = amount + 1

        # min_coins: 금액을 만드는데 필요한 동전 개수를 저장하는 배열
        # min_coins[i]: i원을 만드는데 필요한 최소 동전의 개수
        min_coins = [NOT_POSSIBLE] * (amount + 1)
        min_coins[0] = 0
        
        for cur_amount in range(1, amount + 1):
            # coin: 선택한 동전
            for coin in coins:
                if cur_amount >= coin:
                    # 둘 중 더 작은 값으로 업데이트
                    # 1. 기존에 구한 개수
                    # 2. 현재 동전을 1개 추가해서 만드는 개수
                    min_coins[cur_amount] = min(min_coins[cur_amount], min_coins[cur_amount - coin] + 1)
        
        # 초기화된 값 그대로이면 불가능한 조합이므로 -1 반환
        if min_coins[amount] == NOT_POSSIBLE:
            return -1
        # 최소 동전의 개수를 반환
        else:
            return min_coins[amount]
