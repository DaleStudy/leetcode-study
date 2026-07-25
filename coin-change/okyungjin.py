# coins: 동전의 가격이 적힌 정수 배열, 각 숫자는 유니크함, 정렬에 대한 언급 X, (1 <= coins.length <= 12)
# amount: 돈의 총합

# amount를 만들 수 있는 가장 적은 동전의 수를 반환한다.
# coins로 amount를 만들 수 없는 경우 -1을 반환
# 동전의 종류는 무한대라고 가정하고 문제를 풀 것

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
        
        # 1부터 목표 금액(amount)까지 상향식으로 최소 동전 개수를 계산
        for cur_amount in range(1, amount + 1):
            # 모든 동전 종류를 확인하여 현재 금액을 만들 수 있는 조합 탐색
            for coin in coins:
                # 동전 금액이 현재 금액보다 작거나 같을 때만 유효한 조합으로 간주
                if coin <= cur_amount:
                    # '남은 금액을 만드는 최소 개수' + '현재 동전 1개'를 합산
                    new_val = min_coins[cur_amount - coin] + 1

                    # 더 적은 개수의 동전 조합을 찾았다면 해당 금액의 최솟값을 갱신
                    if new_val < min_coins[cur_amount]:
                        min_coins[cur_amount] = new_val
        
        # 초기화된 값 그대로이면 불가능한 조합이므로 -1 반환
        if min_coins[amount] == NOT_POSSIBLE:
            return -1
        # 최소 동전의 개수를 반환
        else:
            return min_coins[amount]
