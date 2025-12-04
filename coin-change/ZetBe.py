'''
문제: 주어진 동전 종류로 특정 금액을 만들기 위한 최소 동전 개수를 구하시오.
풀이: 동적 계획법(DP)을 사용하여 각 금액에 대해 최소 동전 개수를 계산합니다. 만약 특정 금액을 만들 수 없다면 -1을 반환합니다.
시간 복잡도: O(n * m), n은 금액(amount), m은 동전 종류의 개수입니다. 각 금액에 대해 모든 동전을 확인하므로 전체 시간 복잡도는 O(n * m)입니다.
공간 복잡도: O(n), 금액(amount)까지의 최소 동전 개수를 저장하는 DP 배열을 사용하므로 공간 복잡도는 O(n)입니다.
사용한 자료구조: 배열(DP 배열)
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if len(coins) == 1 and coins[0] > amount:
            return -1
        if amount in coins:
            return 1

        dp = [0 for i in range(amount+1)]
        
        for i in range(amount+1):
            for j in range(len(coins)):
                if i == 0 and coins[j] < amount:
                    dp[coins[j]] = 1
                elif i > 0 and 0 <= i+coins[j] <= amount:
                    if dp[i] > 0 and dp[i+coins[j]] > 0:
                        dp[i+coins[j]] = min(dp[i+coins[j]], dp[i]+1)
                    elif dp[i] > 0 and dp[i+coins[j]] == 0:
                        dp[i+coins[j]] = dp[i]+1
                   



        if dp[amount] == 0:
            return -1
        return dp[amount]


