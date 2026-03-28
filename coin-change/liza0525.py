# 7기 풀이
# 시간 복잡도: O(n * k)
#  - 타겟 코인 값(amount, 복잡도 계산에선 n으로 표기)과 coins의 길이 만큼 탐색하며 계산
# 공간 복잡도: O(n)
#  - 타겟 코인 값(amount, 복잡도 계산에선 n으로 표기) 만큼의 min_coin_count 계산 array를 생성
class Solution:
    # 해당 문제는 현재 갖고 있는 돈으로 각 코인 값을 만드는 데에 동전을 얼마나 쓰는지 계산하여
    # 그 조합 중 가장 작은 값을 계속 찾아가는 문제로, min_coin_count를 사용한다. 
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coin_count = [-1 for _ in range(amount + 1)]  # 각 인덱스는 코인 값, value는 해당 코인 값을 만들 수 있는 동전의 개수(만들 수 없을 땐 -1)
        min_coin_count[0] = 0  # 코인 값이 0일 때는 동전을 쓰지 않으면 되므로 무조건 0이 된다.

        for target_amount in range(1, len(min_coin_count)):
            # 각 코인 값에 대해 최소 동전 개수를 찾는다.
            for coin in coins:
                if target_amount - coin < 0:
                    # 대상 코인 값보다 체크할 코인 값이 큰 경우에는 조합을 만들 수 없으므로 넘긴다
                    continue
                if min_coin_count[target_amount - coin] < 0:
                    # target_amount - coin(보수)을 만들 수 없으면 target_amount도 만들 수 없음
                    # 예시) target=5, coin=3 → 보수 2를 못 만들면 5도 못 만듦
                    continue

                # 위 두 가지 조건만 넘어가면 동전 개수를 min_coin_count[target_amount]에 정해서 넣을 수 있다는 의미
                if min_coin_count[target_amount] == -1:
                    # 값이 -1인 경우에는 처음으로 계산해서 넣는 것이기 때문에
                    # min_coin_count[target_amount - coin]에다가 1을 더해서(coin 한 개를 추가 한다는 의미) min_coin_count[target_amount]에 할당
                    min_coin_count[target_amount] = min_coin_count[target_amount - coin] + 1
                else:
                    # 값이 -1이 아닌 경우는 이전에 저장된 동전 개수가 있으므로
                    # 이전 결과 값과 min_coin_count[target_amount - coin] + 1의 값을 비교하여 더 적은 수를 저장한다.
                    min_coin_count[target_amount] = min(
                        min_coin_count[target_amount],
                        min_coin_count[target_amount - coin] + 1
                    )

        # 모두 계산한 후 min_coin_count[amount]를 반환한다. (== amount를 만드는 동전의 최소 개수)
        return min_coin_count[amount]
